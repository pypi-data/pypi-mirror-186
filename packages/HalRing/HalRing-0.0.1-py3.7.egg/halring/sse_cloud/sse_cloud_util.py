import os
import sys

from loguru import logger

from halring.request.request_util import RequestUtil


class PubCloudTool(object):
    def __init__(self, cloud_url, username, password):

        cloud_instance = {'cloud_url': cloud_url, 'username': username, 'password': password}

        self._cloud_url = cloud_url
        self._username = username
        self._pwd = password

        self._req = RequestUtil()
        self._headers = {"Content-Type": "application/json;charset=UTF-8"}

        # cloud login
        self.cloud_login()

    def cloud_login(self):

        """
        上证云平台登录接口
        :return:
        """
        logger.info("[INF] 初始化")
        logger.info("[INF] 登录容器云平台，获取TOKEN")
        login_url = self._cloud_url + "v1/login"
        post_data = {
            "userName": self._username,
            "password": self._pwd
        }
        login_rsp = self._req.post(login_url, json=post_data).json()
        code = login_rsp["code"]
        data = login_rsp["data"]
        if code == 0:
            logger.info("[INF] 容器云平台登录成功")
            self._headers["Authorization"] = data
        else:
            logger.error("[ERR] " + data)
    
    def external_registries(self):
        get_external_registries_url = self._cloud_url + "v1/external_registries"
        get_data = {
            "name": "test",
            "userName": self._username,
            "password": self._pwd,
            "addr": "artifactory.test.com:8081"
        }
        external_registries_rsp = self._req.post(get_external_registries_url, json=get_data).json()
        code = external_registries_rsp["code"]
        data = external_registries_rsp["data"]
        if code == 0:
            logger.info("[INF] 容器云平台三方库获取成功")
        else:
            logger.error("[ERR] " + data)    

    def get_application(self, app_id):
        """
        上证云应用获取接口
        :param app_id:
        :return:
        """
        get_app_url = self._cloud_url + "v1/apps/" + app_id
        get_data = {
        }
        appinfo_resp = self._req.get(get_app_url, json=get_data, headers=self._headers).json()
        code = appinfo_resp["code"]
        if code == 0:
            logger.info("应用存在")
            return appinfo_resp["data"]
        elif code == 22005:
            logger.info("应用不存在，需新建该应用")
            return None
        else:
            logger.error("获取应用不成功" + appinfo_resp["data"])

    def get_application_status(self, app_id):
        """
        上证云应用获取接口状态
        :param app_id:
        :return:
        """
        get_app_status_url = self._cloud_url + "v1/apps/" + app_id
        get_data = {
        }
        appstatus_resp = self._req.get(get_app_status_url, json=get_data, headers=self._headers).json()
        code = appstatus_resp["code"]
        if "tasksRunning" in appstatus_resp["data"]:
            running_count = appstatus_resp["data"]["tasksRunning"]
            status = "start"
        else:
            running_count = 0
            status = "susspend"
        if code == 0 and running_count > 0:
            logger.info("应用存在，该应用为运行状态")
            return status
        elif code == 0 and running_count == 0:
            logger.info("应用存在，该应用为停止状态")
            return status
        else:
            logger.error("获取应用状态不成功" + appstatus_resp["data"])

    def create_application_start(self, **kwargs):
        """
        新建应用，需要补充参数
        :param kwargs
        :return:
        """
        if kwargs["appid"] is None or kwargs["host_ip"] is None or kwargs["image"] is None:
            logger.error("更新应用不成功, 部署主机地址为空或docker镜像地址为空")
            return "Fail"
        if kwargs["cpus"] is None:
            cpus = 0.2
        else:
            cpus = kwargs["cpus"]
        if kwargs["mem"] is None:
            mem = 1024
        else:
            mem = kwargs["mem"]
        if kwargs["containerPort"] is None:
            container_port = 80
        else:
            container_port = kwargs["containerPort"]
        if kwargs["servicePort"] is None:
            service_port = 10002
        else:
            service_port = kwargs["servicePort"]

        create_app_url = self._cloud_url + "v1/apps/"
        post_data = {
            "id": kwargs["appid"],
            "cmd": None,
            "cpus": cpus,
            "mem": mem,
            "disk": 0,
            "instances": 1,
            "constraints": [
                [
                    "vcluster",
                    "LIKE",
                    "qtp"
                ],
                [
                    "type",
                    "UNLIKE",
                    "swarm"
                ],
                [
                    "hostname",
                    "UNIQUE"
                ],
                [
                    "hostname",
                    "LIKE",
                    kwargs["host_ip"]
                ]
            ],
            "container": {
                "type": "DOCKER",
                "volumes": [

                ],
                "docker": {
                    "image": kwargs["image"],
                    "network": "HOST",
                    "portMappings": [
                        {
                            "containerPort": container_port,
                            "hostPort": 0,
                            "servicePort": service_port,
                            "protocol": "tcp",
                            "name": "http",
                            "labels": {

                            }
                        }
                    ],
                    "privileged": False,
                    "parameters": [

                    ],
                    "forcePullImage": True
                }
            },
            "portDefinitions": [
                {
                    "port": service_port,
                    "protocol": "tcp",
                    "name": "service",
                    "labels": {

                    }
                }
            ],
            "requirePorts": False,
            "backoffSeconds": 1,
            "backoffFactor": 1.15,
            "maxLaunchDelaySeconds": 3600,
            "upgradeStrategy": {
                "minimumHealthCapacity": 1,
                "maximumOverCapacity": 1
            },
            "uris": [
                "http://10.112.4.47:5013/registry_auth/26/43/docker.tar.gz"
            ],
            "labels": {
                "GROUP_ID": "4",
                "USER_ID": "26",
                "VCLUSTER": "qtp"
            }
        }
        appinfo_resp = self._req.post(create_app_url, json=post_data, headers=self._headers).json()
        code = appinfo_resp["code"]
        if code == 0:
            logger.info("[INF] 应用构建成功")
        else:
            logger.error("创建应用不成功" + appinfo_resp["data"])

    def update_application(self, **kwargs):
        """
        上证云更新应用接口
        :param kwargs:
        :return:
        """
        if kwargs["appid"] is None:
            logger.error("更新应用不成功, appid为空")
            return "Fail"
        else:
            update_app_url = self._cloud_url + "v1/apps/" + kwargs["appid"]
        if kwargs["host_ip"] is None or kwargs["image"] is None:
            logger.error("更新应用不成功, 部署主机地址为空或docker镜像地址为空")
            return "Fail"
        if kwargs["cpus"] is None:
            cpus = 0.2
        else:
            cpus = kwargs["cpus"]
        if kwargs["mem"] is None:
            mem = 1024
        else:
            mem = kwargs["mem"]
        if kwargs["containerPort"] is None:
            container_port = 80
        else:
            container_port = kwargs["containerPort"]
        if kwargs["servicePort"] is None:
            service_port = 10002
        else:
            service_port = kwargs["servicePort"]

        put_data = {
            "backoffFactor": 1.15,
            "backoffSeconds": 1,
            "id": kwargs["appid"],
            "cmd": None,
            "cpus": cpus,
            "mem": mem,
            "disk": 0,
            "instances": 1,
            "dependencies": [],
            "labels": {
                "GROUP_ID": "4",
                "USER_ID": "26",
                "VCLUSTER": "qtp"
            },
            "constraints": [
                [
                    "vcluster",
                    "LIKE",
                    "qtp"
                ],
                [
                    "type",
                    "UNLIKE",
                    "swarm"
                ],
                [
                    "hostname",
                    "UNIQUE"
                ],
                [
                    "hostname",
                    "LIKE",
                    kwargs["host_ip"]
                ]
            ],
            "container": {
                "type": "DOCKER",
                "volumes": [],
                "docker": {
                    "image": kwargs["image"],
                    "network": "HOST",
                    "privileged": False,
                    "parameters": [
                        {
                            "key": "label",
                            "value": "APP_ID=qtp-aqc-fxc-server"
                        }
                    ],
                    "forcePullImage": True
                }
            },
            "ports": [service_port],
            "requirePorts": False,
            "portDefinitions": [
                {
                    "port": service_port,
                    "protocol": "tcp",
                    "name": "service",
                    "labels": {

                    }
                }
            ],
            "upgradeStrategy": {"minimumHealthCapacity": 1, "maximumOverCapacity": 1},
            "uris": ["http://10.112.4.47:5013/registry_auth/26/43/docker.tar.gz"]
        }
        appinfo_resp = self._req.put(update_app_url, json=put_data, headers=self._headers).json()
        code = appinfo_resp["code"]
        if code == 0:
            logger.info("[INF] 应用更新成功")
            # app_info = appinfo_resp["data"]
        else:
            logger.error("更新应用不成功" + appinfo_resp["data"])

    def restart_application(self, appid):
        """
        上证云重启应用接口
        :param appid:
        :return:
        """
        restart_app_url = self._cloud_url + "v1/apps/" + appid + "/restart"
        restart_data = {
        }
        appinfo_resp = self._req.post(restart_app_url, json=restart_data, headers=self._headers).json()
        code = appinfo_resp["code"]
        if code == 0:
            logger.info("[INF] 应用重启成功")
            return True
        else:
            logger.error("重启应用不成功" + appinfo_resp["data"])
            return False

    def delete_application(self, appid):
        """
        上证云删除应用接口
        :param appid:
        :return:
        """
        delete_app_url = self._cloud_url + "v1/apps/" + appid
        delete_data = {
        }
        appinfo_resp = self._req.delete(delete_app_url, json=delete_data, headers=self._headers).json()
        code = appinfo_resp["code"]
        if code == 0:
            logger.info("[INF] 应用删除成功")
            return True
        else:
            logger.error("删除应用不成功" + appinfo_resp["data"])
            return False

    def get_stdout(self, appid):
        app_info = pct.get_application(appid)["tasks"][0]
        task_id = app_info["id"]
        node_ip = app_info["ipAddresses"][0]["ipAddress"]
        slave_id = app_info["slaveId"]

        get_stdout_url = self._cloud_url + "v1/tasks/" + task_id + "/" + node_ip + "/" + slave_id + "/stdout"
        stdout_data = {
        }
        stdout_resp = self._req.get(get_stdout_url, json=stdout_data, headers=self._headers)
        code = stdout_resp.status_code
        if code == 200:
            logger.info("[INF] 获取stdout日志成功")
            return stdout_resp.text
        else:
            logger.error("[ERR] 获取stdout日志不成功")
            return False

    def get_stderr(self, appid):
        app_info = pct.get_application(appid)["tasks"][0]
        task_id = app_info["id"]
        node_ip = app_info["ipAddresses"][0]["ipAddress"]
        slave_id = app_info["slaveId"]

        get_stdout_url = self._cloud_url + "v1/tasks/" + task_id + "/" + node_ip + "/" + slave_id + "/stderr"
        stderr_data = {
        }
        stderr_resp = self._req.get(get_stdout_url, json=stderr_data, headers=self._headers)
        code = stderr_resp.status_code
        if code == 0:
            logger.info("[INF] 获取stderr日志成功")
            return stderr_resp.text
        else:
            logger.error("[ERR] 获取stderr日志不成功")
            return False

    def stop_application(self, appid):
        stop_app_url = self._cloud_url + "v1/apps/" + appid
        put_data = {
            "instances": 0
        }
        appinfo_resp = self._req.put(stop_app_url, json=put_data, headers=self._headers)
        if appinfo_resp.status_code == 200:
            logger.info("[INF] 应用停止成功成功")
        else:
            logger.error("[ERR] 应用停止不成功")

    def tool_process(self):
        pass


if __name__ == '__main__':
    pct = PubCloudTool()
    # test_app_id = "qtp-attemper-web"
    # test_app_id = "qtp-spcg-fbmm-front-test"
    test_app_id = ["qtp-spcg-fbmm-front-test"]
    # pct.create_application_start(test_app_id)
    # pct.get_application(test_app_id)
    # pct.get_application_status(test_app_id)
    pct.update_application(appid="qtp-aqc-fxc-server", host_ip="10.112.7.74",
                           image="artifactory.test.com:8081/delivery_docker/fxc/1.3.0/4/spcg-file-exchange-server:1.3.0", cpus=1, mem=1024)
    # pct.delete_application(test_app_id)
    # pct.restart_application(test_app_id)
