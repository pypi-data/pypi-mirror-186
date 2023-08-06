import os
import sys
import traceback
import jenkins
import requests
import json
from halring.log.logging_util import LoggingUtil
from time import sleep
from requests import exceptions

"""
    jenkins_util.py    
    author: ygong
"""


class JenkinsUtil(object):
    def __init__(self, server_ip, user, password):
        self._user = user
        self._password = password
        self._server_ip = server_ip

    def jenkins_login(self):
        self._server = jenkins.Jenkins(self._server_ip, username=self._user, password=self._password)

    def check_job_queue_exist(self, job_name):
        """
        :param job_name: jenkins job的名字
        :return : 若当前有队列，则返回Tue
                  若当前没有队列，则返回False
        """
        queue_item = self._server.get_job_info(job_name)["queueItem"]
        result = True if queue_item else False
        return result

    def check_job_in_building(self, job_name):

        """
        :param job_name: jenkins job的名字
        :return : 若当前有任务正在编译，则返回True
                  若当前没有任务正在编译，则返回False
        """
        last_build_obj = self._server.get_job_info(job_name)["lastBuild"]

        if last_build_obj:
            previous_build_number =last_build_obj["number"]
            previous_build_flag = self._server.get_build_info(job_name, previous_build_number)["building"]
        else:
            previous_build_flag = False
        return previous_build_flag

    def trigger_job_with_file_parameter(self, job_name, job_params_dict, file_params_dict):
        """
        触发jenkins 文件参数构建
        Args:
            job_name: jenkins job的名字
            job_params_dict: 以dict形式传入jenkins job的参数
            file_params_dict: 以dict形式传入jenkins job的文件参数
        Returns: 结果返回build_number
        """

        try:
            next_build_number = self._server.get_job_info(job_name)["nextBuildNumber"]
            '''
            通过requests触发
            '''
            url = "{0}/job/{1}/build".format(self._server_ip, job_name)
            temp_params = []
            for k1 in job_params_dict:
                tmp1 = {"name": k1, "value": job_params_dict[k1]}
                temp_params.append(tmp1)
            # file_name_list=["file"+str(i) for i in range(len(file_params_dict))]
            temp_file_payload_list = []

            for k2 in file_params_dict:
                file_name = k2 + ".tmp"
                tmp2 = {"name": k2, "file": file_name}
                temp_params.append(tmp2)
                temp_file_payload_list.append((file_name, open(file_params_dict[k2], "rb")))
            temp_params = {"parameter": temp_params}
            temp_file_payload_list.append(("json", json.dumps(temp_params)))
            payload = tuple(temp_file_payload_list)

            response = requests.post(url, auth=(self._user, self._password), files=payload)
            build_number = next_build_number
            return build_number
        except Exception as e:
            LoggingUtil().error(traceback.format_exc())
            return 0

    def trigger_job(self, job_name, job_params_dict):
        """
        触发jenkins 构建
        @:param job_name jenkins job的名字
        @:param job_params_dict 以dict形式传入jenkins job的参数
        :return:结果返回build_number
        """
        # 返回 build_number
        try:
            next_build_number = self._server.get_job_info(job_name)["nextBuildNumber"]
            queue_number = self._server.build_job(job_name, job_params_dict)
            # queue number is only valid for 5 min
            build_number = next_build_number
            return build_number
        except jenkins.JenkinsException as e:
            LoggingUtil().error(e.args[0])
            return 0


    def build_job(self, job_name, job_params_dict, timeout=1800, interval=10, max_retry_times=3):
        """
        构建jenkins job
        @:param job_name jenkins job的名字
        @:param job_params_dict 以dict形式传入jenkins job的参数
        @:param timeout 任务超时时间，单位秒，默认为1800秒=30分钟
        @:param interval 轮询任务是否完成间隔，单位秒，默认10秒
        :return:结果返回(build_number,build_result)
        build_result分为 SUCCESS, ABORTED, TIMEOUT, FAILURE
        """
        return self.__build_job_base(job_name, job_params_dict, {}, "common",timeout, interval, max_retry_times)



    def build_job_with_file_parameter(self,job_name, job_params_dict, file_params_dict, timeout=1800, interval=10, max_retry_times=3):

        """
        构建jenkins job
        @:param job_name jenkins job的名字
        @:param job_params_dict 以dict形式传入jenkins job的参数(除文件参数以外的)
        @:param file_params_dict 以dict形式传入jenkins job的文件参数
        @:param timeout 任务超时时间，单位秒，默认为1800秒=30分钟
        @:param interval 轮询任务是否完成间隔，单位秒，默认10秒
        :return:结果返回(build_number,build_result)
        build_result分为 SUCCESS, ABORTED, TIMEOUT, FAILURE
        """
        return self.__build_job_base(job_name, job_params_dict, file_params_dict, "file", timeout, interval, max_retry_times)


    def __build_job_base(self, job_name, job_params_dict, file_params_dict, trigger_type,timeout=1800, interval=10, max_retry_times=3):

        interval = interval
        i_retry_time = 0

        # 等待队列结束，保证queueItem= None
        # 等待队列结束后，等待上一个构建结束

        waiting = 0
        check_job_queue_exist_result = self.check_job_queue_exist(job_name)

        while check_job_queue_exist_result and i_retry_time <= max_retry_times:
            try:
                check_job_queue_exist_result = self.check_job_queue_exist(job_name)
                i_retry_time = 0
            except exceptions.ConnectionError:
                i_retry_time = i_retry_time + 1
                log_content = "连接断开，重试次数：" + str(i_retry_time)
                check_job_queue_exist_result = "connection aborted"
                LoggingUtil().warning(log_content)
                continue

            LoggingUtil().info("Waiting previous queue item build complete")
            sleep(interval)
            waiting = waiting + interval

            if waiting >= timeout:
                LoggingUtil().error("Previous queue item build timeout")
                return (0, "TIMEOUT")

        if check_job_queue_exist_result == "connection aborted":
            return (0, "TIMEOUT")

        i_retry_time = 0
        check_job_in_building_result = self.check_job_in_building(job_name)

        while check_job_in_building_result and i_retry_time <= max_retry_times:
            try:
                check_job_in_building_result = self.check_job_in_building(job_name)
                i_retry_time = 0
            except exceptions.ConnectionError:
                i_retry_time = i_retry_time + 1
                log_content = "连接断开，重试次数：" + str(i_retry_time)
                check_job_in_building_result = "connection aborted"
                LoggingUtil().warning(log_content)
                continue

            LoggingUtil().info("Waiting previous job build complete")
            sleep(interval)
            waiting = waiting + interval

            if waiting >= timeout:
                LoggingUtil().error("Previous job build timeout")
                return (0, "TIMEOUT")

        if check_job_in_building_result == "connection aborted":
            return (0, "TIMEOUT")

        # 触发构建，最大重试次数为3次
        i_retry_time = 0
        while i_retry_time <= max_retry_times:
            try:
                if trigger_type=="file":
                    build_number = self.trigger_job_with_file_parameter(job_name, job_params_dict, file_params_dict)
                else:
                    build_number = self.trigger_job(job_name, job_params_dict)

                i_retry_time = 0
                break
            except exceptions.ConnectionError:
                i_retry_time = i_retry_time + 1
                log_content = "连接段开，重试次数：" + str(i_retry_time)
                LoggingUtil().warning(log_content)
                continue

        # 如果i_retry_time 已大于最大重试次数，则说明在重试次数内未连接上目标服务器，也未成功触发构建
        if i_retry_time > max_retry_times:
            build_number = 0

        # 如果触发由于其他意外退出导致build_number = 0
        if build_number == 0:
            LoggingUtil().error("Trigger failed")
            return (build_number, "ERROR")

        LoggingUtil().info("Start building:" + job_name)
        LoggingUtil().info("Build number:" + str(build_number))

        # 等待到可以获取result信息
        result = self.jenkins_get_build_info_with_waiting(job_name, build_number)

        if result == "timeout":
            LoggingUtil().error("Get build info failed")
            return (build_number, "ERROR")

        # 初始building状态设为True
        building_flag = True

        while building_flag and i_retry_time <= max_retry_times:
            try:
                building_flag = self._server.get_build_info(job_name, build_number)["building"]
                i_retry_time = 0
            #   not subClass of OSError ConnectionError
            except exceptions.ConnectionError as e:
                i_retry_time = i_retry_time + 1
                log_content = "连接断开，重试次数：" + str(i_retry_time)
                LoggingUtil().warning(log_content)
                continue

            building_status = "building" if building_flag else "finish"
            sleep(interval)
            waiting = waiting + interval

            LoggingUtil().info("Check job build status:" + building_status)

            if waiting >= timeout:
                LoggingUtil().error("Job builds timeout")
                return (build_number, "TIMEOUT")

        # 编译结束,返回编译结果
        if not building_flag:
            build_result = self._server.get_build_info(job_name, build_number)["result"]
            # SUCCESS
            # ABORTED
            # FAILURE
            return (build_number, build_result)

    def check_job_in_building_with_retry(self, job_name, retry_times=3):
        """
        :param job_name: jenkins job的名字
        :param retry_times:默认是3,连接不上时的重试次数
        :return:  若当前有任务正在编译，则返回True
                  若当前没有任务正在编译，则返回False
                  超过重试次数，返回timeout
        """
        return self.function_with_retry(retry_times, self.check_job_in_building, job_name=job_name)

    def check_job_queue_exist_with_retry(self, job_name, retry_times=3):
        """
        :param job_name:jenkins job的名字
        :param retry_times:默认是3,连接不上时的重试次数
        :return:若当前有队列，则返回True
                若当前没有队列，则返回False
                超过重试次数，返回timeout
        """
        return self.function_with_retry(retry_times, self.check_job_queue_exist, job_name=job_name)

    def jenkins_get_build_info_with_retry(self, job_name, job_build, retry_times=3):
        """
        获取job build info
        @:param job_name: jenkins job的名字
        @:param job_build: jenkins job的build号
        :return:结果返回同get_build_info
                超过重试次数，返回timeout
        """
        return self.function_with_retry(retry_times, self.jenkins_get_build_info, job_name=job_name, job_build=job_build)

    def jenkins_get_job_info_with_retry(self, job_name, retry_times=3):
        """
        获取job info
        :param job_name:
        :param retry_times:
        :return:
        """

        return self.function_with_retry(retry_times, self.jenkins_get_job_info, job_name=job_name)

    @staticmethod
    def function_with_retry(retry_times, fun, **kwargs):
        i_retry_time = 0
        while i_retry_time <= retry_times:
            try:
                return fun(**kwargs)
            except exceptions.ConnectionError:
                i_retry_time = i_retry_time + 1
                log_content = "连接断开，重试次数：{0}.".format(i_retry_time)
                LoggingUtil().info(log_content)
                continue
        return "timeout"

    def jenkins_get_job_info(self, job_name):
        """
        获取job info
        @:param job_name jenkins job的名字
        :return:结果返回同get_job_info
        """
        return self._server.get_job_info(job_name)

    def jenkins_get_build_info(self, job_name, job_build):
        """
        获取job build info
        @:param job_name: jenkins job的名字
        @:param job_build: jenkins job的build号
        :return:结果返回同get_build_info
        """
        return self._server.get_build_info(job_name, job_build)

    def jenkins_get_queue_info(self):
        """
        获取jenkins server所有在队列中等待的任务信息
        :return:结果返回同get_queue_info
        """
        return self._server.get_queue_info()

    def jenkins_get_build_console_output(self, job_name, job_build):
        """
        :param job_name: jenkins job的名字
        :param job_build: jenkins job的build号
        :return: 结果返回同get_build_console_output(如果slave机是win系统则返回日志可能有乱码)
        """
        return self._server.get_build_console_output(job_name, job_build)

    def jenkins_get_build_info_with_waiting(self, job_name, build_number, interval=3, timeout=180):

        waiting = 0
        while waiting < timeout:
            try:
                result = self.jenkins_get_build_info_with_retry(job_name, build_number)
                return result
            except jenkins.JenkinsException as e:

                #   如果未获取到对应build,检查正在build的里是否有正在队列的
                job_info = self.jenkins_get_job_info_with_retry(job_name)
                current_build_number = job_info.get("lastBuild").get("number")
                queue_item_number = int(len(job_info.get("queueItem"))) if job_info.get("queueItem") else 0
                if build_number > current_build_number + queue_item_number:
                    raise e
                else:
                    #   循环等待队列
                    sleep(interval)
                    waiting = waiting + interval
                    continue
        return "timeout"




if __name__ == '__main__':
    jk_util= JenkinsUtil("http://10.112.6.207:8080","admin","Cvsopuser@2019")
    result = jk_util.jenkins_login()
    a=jk_util.build_job_with_file_parameter("4test",{"test":"555"},{
    "file.txt":"C:\\Users\\ygong.SSE\\Downloads\\package.info",
    "file1.txt": "C:\\Users\\ygong.SSE\\Downloads\\packtools.sh",
})
    print(a)
