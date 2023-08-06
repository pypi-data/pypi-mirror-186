# -*- coding:UTF-8 -*-
"""

Title:
    apollo_opr_util

Author:
    rzzhou

Fuctions:
    1、指定项目、指定环境，对某一配置做增、删、改、查\n
    2、指定项目、指定环境，获取所有配置列表\n
    3、指定项目，获取所有环境列表\n
    4、获取所有项目列表\n
    5、指定项目、指定环境，检查配置是否存在（存在标准为至少有1条配置）\n
    6、从指定格式文件导入批量配置，覆盖指定项目、指定环境的配置。\n
    7、指定项目、指定环境，导出所有配置。\n

"""
import os
import sys
from halring.log.loguru_util import LoguruUtil
# halring_root = os.path.abspath(__file__).split("apollo")[0]
# sys.path.append(halring_root)
# from log.loguru_util import LoguruUtil
import requests
import json
import traceback
class ApolloOprUtil:
    def __init__(self,apolloServer,apolloToken,apolloUser):
        """
        初始化

        Args:
            apolloServer: 操作的apollo服务器ip
            apolloToken: 操作权限token
            apolloUser: 操作的uums-配置中心账号
        """
        self._apollo_server = apolloServer
        self._apollo_token = apolloToken
        self._apollo_user = apolloUser
        self._apollo_openapi = apolloServer + "/openapi/v1/"
        self.logger = LoguruUtil()

        self._http_headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization": self._apollo_token}
        token_avaliable = self.get_apps()
        if not token_avaliable.ok:
            self.logger.error("token error")
            sys.exit(-1)
        else:
            self.logger.success("token is ok")


    def get_apps(self, appid=None):
        """
        获取项目app信息

        Args:
            appid(str): 项目app,可以为空

        Returns:
            response(Response): 接口request方法的response对象
        """

        request_url = self._apollo_openapi+"apps"

        if appid is None:
            request_response = requests.get(request_url,headers=self._http_headers)
        else:
            set_payload_data = {"appIds":str(appid)}
            #json_s = json.dumps(set_payload_data)
            request_response = requests.get(request_url, params=set_payload_data, headers=self._http_headers)#get请求的参数用 params


        return request_response


    def get_appid_env_clusters(self,appid):
        """
        获取App的环境，集群信息

        Args:
            appid(str): apollo中项目的key,不可为空

        Returns:
            response(Response): 接口request方法的response对象

        """

        request_url = self._apollo_openapi+"apps/"+str(appid)+"/envclusters"
        request_response = requests.get(request_url, headers=self._http_headers)

        return request_response

    def check_appid_env_exist(self,appid,env):
        """
        判断应用(appid)的环境(env)是否存在

        Args:
            appid: 项目app,非空
            env: 项目环境,非空

        Returns:
            bool

        """

        return_result = False
        request_url = self._apollo_openapi+"apps/"+str(appid)+"/envclusters"
        request_response = requests.get(request_url, headers=self._http_headers)
        if str(request_response.raw.status) == str("200"):
            response_text = request_response.text
            result_list = json.loads(response_text)
            if len(result_list) > 0:
                for item in result_list:
                    item_env = item.get("env")
                    if str(env) == str(item_env):
                        return_result = True
            else:
                return_result = False

        else:
            return_result = False

        return return_result

    def check_appid_env_cluster_exist(self,appid,env,cluster):
        """
        判断应用(appid)的环境(env)中的 集群 (cluster)是否存在

        Args:
            appid: 项目app
            env: 项目环境
            cluster: 项目集群

        Returns:
            True or False
        """
        return_result = False
        request_url = self._apollo_openapi + "apps/" + str(appid) + "/envclusters"
        request_response = requests.get(request_url, headers=self._http_headers)
        if str(request_response.raw.status) == str("200"):
            response_text = request_response.text
            result_list = json.loads(response_text)
            if len(result_list) > 0:
                for item in result_list:
                    item_env = item.get("env")
                    if str(env) == str(item_env):
                        item_cluster = item.get("clusters")
                        if isinstance(item_cluster, list):
                            if str(cluster) in item_cluster:
                                return_result = True

                        elif isinstance(item_cluster, str):
                            if str(cluster) == str(item_cluster):
                                return_result = True

        else:
            return_result = False

        return return_result

    def get_appid_env_cluster_namespace(self,appid,env,cluster,namespace=None):
        """
        获取项目下的指定环境集群的Namespace

        Args:
            appid: 项目
            env: 项目环境
            cluster: 项目集群
            namespace: 项目配置集

        Returns:
            response对象:
        """

        try:
            if namespace is None:
                request_url = self._apollo_openapi + "envs/" +str(env) + "/apps/" + str(appid) + "/clusters/"+ str(cluster) +"/namespaces"
                request_response = requests.get(request_url, headers=self._http_headers)

            else:
                request_url = self._apollo_openapi + "envs/" +str(env) + "/apps/" + str(appid) + "/clusters/"+ str(cluster) +"/namespaces/"+namespace
                request_response = requests.get(request_url, headers=self._http_headers)

            return request_response

        except Exception as e:
            self.logger.error(e)
            self.logger.error(traceback.format_exc())


    def check_appid_env_cluster_namespace_exist(self,appid,env,cluster,namespace):
        """
        检查项目下指定环境的配置集是否存在

        Args:
            appid:项目应用
            env:项目环境
            cluster:集群
            namespace:配置集

        Returns:
            true or false
        """

        try:
            request_url = self._apollo_openapi + "envs/" + str(env) + "/apps/" + str(appid) + "/clusters/" + str(
                cluster) + "/namespaces/" + namespace

            request_result = requests.get(request_url, headers=self._http_headers)

            if str(request_result.raw.status) == "200":
                return True
            else:
                return False

        except Exception as e:
            self.logger.error(e)
            self.logger.error(traceback.format_exc())

    def check_appid_namespace_item_exist(self,appid,env,cluster,namespace,itemkey):
        """
        检查项目应用的配置集中的配置项是否存在

        Args:
            appid: 项目应用
            env:  环境
            cluster:  集群
            namespace:  配置集
            itemkey: 配置项的名字

        Returns:
            True or False
        """

        try:
            request_url = self._apollo_openapi +"envs/"+str(env)+"/apps/"+str(appid)+"/clusters/"+str(cluster)+"/namespaces/"+str(namespace)+"/items/"+str(itemkey)

            request_result = requests.get(request_url, headers=self._http_headers)

            if str(request_result.raw.status) == "200":
                return True
            else:
                return False
        except Exception as e:
            self.logger.error(e)
            self.logger.error(traceback.format_exc())



    def get_appid_namespace_item(self,appid,env,cluster,namespace,itemkey):
        """
        获取项目配置集中的某个配置

        Args:
            appid: 项目应用
            env: 环境
            cluster: 集群
            namespace: 配置集
            itemkey: 配置名

        Returns:
            response对象
        """

        try:
            request_url = self._apollo_openapi + "envs/" + str(env) + "/apps/" + str(appid) + "/clusters/" + str(
                cluster) + "/namespaces/" + str(namespace) + "/items/" + str(itemkey)

            request_result = requests.get(request_url, headers=self._http_headers)

            return request_result

        except Exception as e:
            self.logger.error(e)
            self.logger.error(traceback.format_exc())

    def add_appid_namespace_item(self,appid,env,cluster,namespace,itemkey,itemvalue,comment=None):
        """
        新增指定配置集中的字段
        Args:
            appid: 项目app,非空
            env: 项目环境,非空
            cluster: 项目集群,非空
            namespace: 项目配置集名,非空
            itemkey: 配置字段名,非空
            itemvalue: 配置字段值,非空
            comment: 字段评论,可以为空

        Returns:
            response对象
        """
        try:
            request_url = self._apollo_openapi + "envs/" + str(env) + "/apps/" + str(appid) + "/clusters/" + str(
                cluster) + "/namespaces/" + str(namespace) + "/items"
            if comment is None:
                post_data = {"key":str(itemkey), "value":str(itemvalue), "dataChangeCreatedBy":str(self._apollo_user)}
            else:
                post_data = {"key":str(itemkey), "value":str(itemvalue), "comment":str(comment), "dataChangeCreatedBy":str(self._apollo_user)}
            json_data = json.dumps(post_data)

            request_result = requests.post(request_url, data=json_data, headers=self._http_headers)

            return request_result
        except Exception as e:
            self.logger.error(e)
            self.logger.error(traceback.format_exc())

    def modify_appid_namespace_item(self,appid,env,cluster,namespace,itemkey,itemvalue,comment=None):
        """
        修改项目配置集中的一个配置项

        Args:
            appid: 项目应用
            env:  环境
            cluster:  集群
            namespace:  配置集
            itemkey:  配置项名
            itemvalue:  配置项值
            comment:  评论

        Returns:
            response对象
        """

        try:
            request_url = self._apollo_openapi + "envs/" + str(env) + "/apps/" + str(appid) + "/clusters/" + str(
                cluster) + "/namespaces/" + str(namespace) + "/items/" + str(itemkey)
            if comment is None:
                param_data ={"key": str(itemkey),"value": str(itemvalue),"dataChangeLastModifiedBy":str(self._apollo_user) }
            else:
                param_data ={"key": str(itemkey),"value": str(itemvalue),"comment": str(comment),"dataChangeLastModifiedBy":str(self._apollo_user) }
            json_data = json.dumps(param_data)

            request_result = requests.put(request_url, data=json_data, headers=self._http_headers)

            return request_result

        except Exception as e:
            self.logger.error(e)
            self.logger.error(traceback.format_exc())

    def delete_appid_namespace_item(self,appid,env,cluster,namespace,itemkey):
        """
        删除配置集中的配置项

        Args:
            appid: 项目应用
            env: 环境
            cluster: 集群
            namespace: 配置集
            itemkey: 配置项的名

        Returns:
            response对象
        """

        try:
            request_url = self._apollo_openapi + "envs/"+ str(env)+"/apps/"+str(appid)+"/clusters/"+str(cluster)+"/namespaces/"+str(namespace)+"/items/"+str(itemkey)
            param_data = {"key": str(itemkey),"operator": str(self._apollo_user) }

            request_result = requests.delete(request_url,params=param_data,headers=self._http_headers)

            return request_result

        except Exception as e:
            self.logger.error(e)
            self.logger.error(traceback.format_exc())


    def release_apppid_namespace(self,appid,env,cluster,namespace,release_title,release_comment=None):
        """
        发布指定项目的配置

        Args:
            appid: 项目名
            env: 环境
            cluster: 集群
            namespace: 配置集
            release_title: 发布名
            release_comment: 发布评论

        Returns:
            response对象
        """
        try:
            request_url = self._apollo_openapi + "envs/"+ str(env) +"/apps/"+ str(appid)+ "/clusters/"+ str(cluster) + "/namespaces/" + str(namespace)+"/releases"
            if release_comment is None:
                param_body = {"releaseTitle": str(release_title), "releasedBy": str(self._apollo_user)}
            else:
                param_body = {"releaseTitle": str(release_title), "releaseComment": str(release_comment), "releasedBy": str(self._apollo_user)}
            request_body = json.dumps(param_body)

            request_response = requests.post(request_url,data=request_body,headers=self._http_headers)


            return request_response


        except Exception as e:
            self.logger.error(e)
            self.logger.error(traceback.format_exc())

    def get_latest_released_namespace(self,appid,env,cluster,namepsacename):
        """
        获取某个已发布的配置集的口

        Args:
            appid:  项目
            env:  环境
            cluster:  集群
            namepsacename: 配置集的名字

        Returns:
            response对象
        """
        try:
            request_url = self._apollo_openapi + "envs/"+str(env) +"/apps/"+str(appid)+"/clusters/"+str(cluster)+"/namespaces/"+str(namepsacename)+"/releases/latest"
            request_response = requests.get(request_url,headers=self._http_headers)
            return request_response
        except Exception as e:
            self.logger.error(e)
            self.logger.error(traceback.format_exc())


    def import_appid_namespace(self, appid, env, cluster, namespacename, inputdict, reset=False):
        """
        导入一个字典的内容作为配置集
        1.配置集本身必须存在
        2.配置集与输入字典相比同名的item进行修改
        3.配置集与输入字典相比不存在的item进行新建
        4.配置集与输入字典相比多余的item进行删除?

        Args:
            appid: 应用
            env: 环境
            cluster: 集群
            namespacename: 配置集名必须为已有
            inputdict: 待导入的字典，是只取key-value
        Returns:
            {itemkey:itemvalue}
        """
        try:

            if len(inputdict.keys()) >0:#校验输入字典有效
                target_item_list = inputdict.keys()
                modify_item_dict = {}#初始化预修改item的字典
                add_item_dict = {}#初始化预新增item的字典
                delete_item_dict = {}#初始化预删除item的字典
                get_namespace_response = self.get_appid_env_cluster_namespace(appid,env,cluster,namespacename) #获取当前namespace

                if get_namespace_response.ok:
                    current_namespace = json.loads(get_namespace_response.text)
                    current_namespace_items = current_namespace.get("items")
                    if len(current_namespace_items) >0:
                        source_item_list =[]
                        for item_object in current_namespace_items:
                            item_key = item_object.get("key")
                            source_item_list.append(item_key)
                            if item_key in target_item_list:#配置集中存在与输入字典同名的item
                                if item_object.get("value") != inputdict.get(item_key): #item值不同
                                    modify_item_dict[item_key] = inputdict.get(item_key)  #存入预修改的字典

                            else: #配置集中有，而输入字典没有的item
                                delete_item_dict[item_key] = inputdict.get(item_key)

                        for item_key in target_item_list:
                            if item_key not in source_item_list: #输入字典中有而配置集中没有的item
                                add_item_dict[item_key] = inputdict.get(item_key)

                    else:#配置集中item为空，则全部新增
                        add_item_dict = inputdict

                    """进行批量处理"""

                    if add_item_dict.keys() is not None:
                        for add_key in add_item_dict.keys():
                            add_value = add_item_dict.get(add_key)
                            self.add_appid_namespace_item(appid,env,cluster,namespacename,add_key,add_value)

                    if modify_item_dict.keys() is not None:
                        for modify_key in modify_item_dict.keys():
                            modify_value = modify_item_dict.get(modify_key)
                            self.modify_appid_namespace_item(appid,env,cluster,namespacename,modify_key,modify_value)

                    if reset and delete_item_dict.keys() is not None:
                        for delete_key in delete_item_dict.keys():
                            self.delete_appid_namespace_item(appid,env,cluster,namespacename,delete_key)

                    return_status =True
                    return_value = self.export_appid_namespace(appid,env,cluster,namespacename).get("value")
                else:
                    return_status =False

            else:
                return_status = False
                return_value = None

            return return_value
        except Exception as e:
            self.logger.error(e)
            self.logger.error(traceback.format_exc())

    def export_appid_namespace(self, appid, env, cluster, namespacename):
        """
        导出目标配置集的内容到dict中返回

        Args:
            appid: 应用
            env: 环境
            cluster: 集群
            namespacename: 配置集

        Returns:
            {itemkey:itemvalue}

        """
        try:

            get_response = self.get_appid_env_cluster_namespace(appid, env, cluster, namespacename)
            if get_response.ok:
                return_status = True
                namespace_content = json.loads(get_response.text)

                item_list = namespace_content.get("items")
                item_dict = {}
                if len(item_list) > 0:
                    for item_object in item_list:
                        item_key = item_object.get("key")
                        item_value = item_object.get("value")
                        item_dict[item_key] = item_value
                return_value = item_dict

            else:
                return_status = False
                return_value = None

            return return_value
        except Exception as e:
            self.logger.error(e)
            self.logger.error(traceback.format_exc())

    def export_latest_releasd_appid_namespace(self,appid,env,cluster,namespacename):
        """
        导出已发布的目标配置集的内容到dict中返回

        Args:
            appid: 应用
            env: 环境
            cluster: 集群
            namespacename: 配置集

        Returns:
            {itemkey:itemvalue}

        """
        try:

            namespace_content = self.get_latest_released_namespace(appid,env,cluster,namespacename)
            if namespace_content.get("status"):
                return_status = True
                namespace_value = namespace_content.get("value")
                item_list = namespace_value.get("items")
                item_dict = {}
                if len(item_list)>0:
                    for item_object in item_list:
                        item_key = item_object.get("key")
                        item_value = item_object.get("value")
                        item_dict[item_key] = item_value
                return_value = item_dict

            else:
                return_status = False
                return_value = None

            return return_value
        except Exception as e:
            self.logger.error(e)
            self.logger.error(traceback.format_exc())



    def export_latest_released_appid_namespace(self, appid, env, cluster, namespacename):
        """
        导出已发布的目标配置集的内容到dict中返回

        Args:
            appid: 应用
            env: 环境
            cluster: 集群
            namespacename: 配置集

        Returns:
            {itemkey:itemvalue}

        """
        try:

            get_response = self.get_latest_released_namespace(appid, env, cluster, namespacename)
            if get_response.ok:
                return_status = True
                if get_response.text != "":
                    namespace_content = json.loads(get_response.text)
                    return_value = namespace_content.get('configurations')
                else:
                    return_value = ""


            else:
                return_status = False
                return_value = None

            return return_value
        except Exception as e:
            self.logger.error(e)
            self.logger.error(traceback.format_exc())

