# -*- coding:UTF-8 -*-
"""
__title__ = ''
__author__ = 'wu.keke'
__mtime__ = '2020/4/13'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
JIRA基础库需求
1.取出单个单子的整个对象，输入：单子KEY 例：NADDONTEST-584
2.更新指定单子的指派人，字段值
3.流转某个单子
4.新建单子 ，用单子内容用对象
5.根据JQL ，指定field,获得所有单子的对象列表

"""
import time
import traceback
import urllib

import requests
import json
from requests.auth import HTTPBasicAuth
from jira import JIRA
from loguru import logger

# noinspection PyShadowingNames,PyIncorrectDocstring,PyMethodMayBeStatic
class JiraUtil:
    def __init__(self,jiraUser=None, jiraPass=None,jiraServer=None):
        """

        :param jiraUser: 可传入自己的用户名
        :param jiraPass: 可传讹入自己的密码
        """

        self.server = jiraServer if jiraServer is not None else 'http://eqops.tc.com/jira/'

        # 生产环境
        # self.server = 'http://eqops.tc.com/jira/'
        # 测试环境
        # self.server = 'http://10.112.6.16:8080/jira/'
        self.basic_auth = (
            jiraUser, jiraPass)
        self.jiraClient = None
    def login(self):
        """
         登录jira
        function used for login
        :__Author__ : wu.keke
        :__mtime__ : 2020/4/2 14:03

        :return:
        """
        self.jiraClient = JIRA(server=self.server, basic_auth=self.basic_auth)

        if self.jiraClient is not None:
            return True
        else:
            return False

    def getAllProjects(self):
        """
        获取所有项目
        function used for
        :__Author__ : wu.keke
        :__mtime__ : 2020/4/16 15:45
        """
        return self.jiraClient.projects()

    def getProjectById(self, project_id):
        """

        :param project_id:项目id
        :return:

        根据项目id,获取指定的项目
        function used for
        :__Author__ : wu.keke
        :__mtime__ : 2020/4/16 15:45
        """
        return self.jiraClient.project(project_id)

    def getProjectByKey(self, project_key):
        """

        :param project_key: 项目的key
        :return:

        根据项目key,获取指定的项目
        function used for
        :__Author__ : wu.keke
        :__mtime__ : 2020/4/16 15:45
        """
        return self.jiraClient.project(project_key)

    def projectIsExist(self, project_key):
        '''
            根据 key 判断项目是否存在
        :param project_key: 比如 :NADDONTEST
        :return: boolean
        '''
        try:
            self.jiraClient.project(project_key)
        except Exception as ex:
            return False

        return True

    def getProjectVerById(self, project_id):
        """

        :param project_id: 项目的id
        :return:

        根据项目id,获取指定的项目的所有版本信息
        function used for
        :__Author__ : wu.keke
        :__mtime__ : 2020/4/16 15:45
        """
        # for ver in self.jiraClient.project(project_id).versions:
        #     print(ver)

        return self.jiraClient.project(project_id).versions

    def getProjectsInfo(self):
        """
        获取所有项目信息,仅仅打印在控制台,无返回值
        function used for
        :__Author__ : wu.keke
        :__mtime__ : 2020/4/16 15:45
        """
        for p in self.jiraClient.projects():
            print(p, p.id, p.name)

    def search_issues(self, jql, maxResults=None):
        """
        根据jql查询问题单,查出所有问题单列表

        :param jql:  自定义jql语句
        :param maxResults: maxResults为一次最大查询数量参数,整型数字
                           1.maxResults可不传,不传此参数默认一次查询200,直到查询所有结束,返回结果;
                           2.传此参数,则使用该值作为一次最大查询数量,直到查询所有结束,返回结果;
                           3.注意 maxResults经本机测试最大不得超过 2147483647,否则直接报错
        :return: dict status:True or False And result: issuesList
        """
        result = {}
        try:
            maxResult = maxResults if maxResults is not None else 200
            issuesList = []
            got = maxResult
            total = 0
            while got == maxResult:
                issues = self.jiraClient.search_issues(jql, maxResults=maxResult, startAt=total)
                got = len(issues)
                total += got
                for i in issues:
                    issuesList.append(i)
            result["status"] = True
            result["result"] = issuesList
            return result

        except Exception as ex:
            logger.error("\tError %s\n" % ex)
            logger.error(traceback.format_exc())
            result["status"] = False
            result["result"] = issuesList
            return result

    def search_issues_limit(self, jql, startAt=None, maxResults=None):
        """

        :param jql: 自定义jql语句查询,说明: 从第几个开始查,查询多少条
        :param startAt: 自定义从第几条开始查,不得超过总数,超过查询结果总数则为空,传None时默认从0开始查询
        :param maxResults: 查询最大条数,不传此参数.默认查询所有
        :return: issues
        """

        maxResult = maxResults if maxResults is not None else 0
        issues = self.jiraClient.search_issues(jql, maxResults=maxResult, startAt=startAt)

        return issues

    def issue(self, param):

        """

        :param param: 问题单key或id
        :return:issue

        获取指定的问题单
        function used for
        :__Author__ : wu.keke
        :__mtime__ : 2020/4/15 15:22
        """
        return self.jiraClient.issue(param)

    def create_issue(self, issue_dict):
        """
        issue_dict={'project':{'key':project},

                   'issuetype':{'name':issuetype},

                   '''

                   '''
                   }

        :param issue_dict:dict
        :return:

        创建问题单,自定义 ,用户需对issue_dict各字段值了解
        function used for
        :__Author__ : wu.keke
        :__mtime__ : 2020/4/15 15:22
        """
        return self.jiraClient.create_issue(issue_dict)

    def update_issue(self, key, issue_dict):
        """

        :param key: 问题单key
        :param issue_dict:dict
        :return: True or False

        修改问题单
        function used for
        :__Author__ : wu.keke
        :__mtime__ : 2020/4/15 15:22
        """

        try:
            self.issue(key).update(fields=issue_dict)
        except Exception as ex:
            logger.error("\tError %s\n" % ex)
            logger.error(traceback.format_exc())
            return False
        return True

    def updateAssignee(self, key, name):
        """

        :param key:project_key
        :param name:value
        :return: True or False

        根据项目的key,修改经办人
        function used for
        :__Author__ : wu.keke
        :__mtime__ : 2020/4/15 15:22
        """
        try:
            self.issue(key).update(assignee={'name': name})
        except Exception as ex:
            logger.error("\tError %s\n" % ex)
            logger.error(traceback.format_exc())
            return False
        return True

    def getIssues(self, jql, field):
        """
        带field的查询方法
        :param jql:
        :param field:
        :return:
        """
        return self.jiraClient.search_issues(jql, fields=field)

    def getProjectRoles(self,projectKey):
        """
        查询某项目的所有的角色
        :param projectKey:  项目的Key
        :return: {角色名:{'id':'角色id','url':'该角色详情的url'}}
        """
        return self.jiraClient.project_roles(projectKey)

    def getProjectRoleByRoleid(self,projectKey,roleid):
        """
        查询某项目的某角色的信息
        :param projectKey: 项目的Key
        :param roleid:
        :return: Role对象
        """
        return self.jiraClient.project_role(projectKey,roleid)

    def addProjectRoleActor(self,projectKey,roleid,username):
        """
        设置某个项目的角色为某个用户
        :param projectKey: 项目的Key
        :param roleid: 目标设置的Role的ID
        :param username: 目标设置的用户名
        :return: 设置成功
        """

        headers = {"Content-Type":"application/json;charset=UTF-8"}
        set_payload_list ={'user':[username]}
        #form_payload = urllib.parse.urlencode(payload).encode(encoding='utf-8')
        json_s = json.dumps(set_payload_list)
        r = requests.post(self.server+"/rest/api/2/project/"+projectKey+"/role/"+roleid,data=json_s,auth=self.basic_auth,headers=headers)
        return r

    def addProjectRoleActors(self,projectKey,roleid,actornames):
        actors_list = actornames.split("|")

        headers = {"Content-Type": "application/json;charset=UTF-8"}
        set_payload_list = {'user': list(actors_list)}
        # form_payload = urllib.parse.urlencode(payload).encode(encoding='utf-8')
        json_s = json.dumps(set_payload_list)
        r = requests.post(self.server + "/rest/api/2/project/" + projectKey + "/role/" + roleid, data=json_s,
                          auth=self.basic_auth, headers=headers)
        return r

    def addProjectRoleGroups(self,projectKey,roleid,groupnames):

        actors_list = groupnames.split("|")

        headers = {"Content-Type": "application/json;charset=UTF-8"}
        set_payload_list = {'group': list(actors_list)}
        # form_payload = urllib.parse.urlencode(payload).encode(encoding='utf-8')
        json_s = json.dumps(set_payload_list)
        r = requests.post(self.server + "/rest/api/2/project/" + projectKey + "/role/" + roleid, data=json_s,
                          auth=self.basic_auth, headers=headers)
        return r

    def delProjectRoleActor(self,projectKey,roleid,username):
        """
        删除指定项目中的角色
        :param projectKey:项目的Key
        :param roleid: 删除目标的角色id
        :param username: 需要删除角色中的用户名
        :return:
        """
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        param_payload = { 'user': username}
        r = requests.delete(self.server+"/rest/api/2/project/"+projectKey+"/role/" + roleid,params=param_payload,auth=self.basic_auth,headers=headers)
        return r

    def delProjectRoleGroup(self,projectKey,roleid,groupname):
        """
        删除指定项目中的组
        :param projectKey: 项目的Key
        :param roleid: 删除目标的角色id
        :param groupname: 组名
        :return:
        """
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        param_payload = {'group': groupname}
        r = requests.delete(self.server + "/rest/api/2/project/" + projectKey + "/role/" + roleid, params=param_payload,
                            auth=self.basic_auth,headers=headers)
        return r

    def addProjectRoleGroup(self,projectKey,roleid,groupname):
        """
        设置某个项目的角色为某个用户
        :param projectKey: 项目的Key
        :param roleid: 目标设置的Role的ID
        :param username: 目标设置的用户名
        :return: 设置成功
        """

        headers = {"Content-Type":"application/json;charset=UTF-8"}
        set_payload_list ={'group':[groupname]}
        #form_payload = urllib.parse.urlencode(payload).encode(encoding='utf-8')
        json_s = json.dumps(set_payload_list)
        r = requests.post(self.server+"/rest/api/2/project/"+projectKey+"/role/"+roleid,data=json_s,auth=self.basic_auth,headers=headers)
        return r

    def get_user_is_exist(self,username):
        """
        根据用户名获取用户
        :param username: 域账号
        :return: True or False
        """
        r = requests.get(self.server+"/rest/api/2/user/",params={'username':username},auth=self.basic_auth)
        return r.ok

    def get_group_is_exist(self,groupname):
        """
        根据用户名获取用户
        :param groupname: 组名
        :return: True or False
        """
        r = requests.get(self.server+"/rest/api/2/group/",params={'groupname':groupname},auth=self.basic_auth)
        return r.ok

    def search_project_all_rolenames(self,projectKey):
        """
        查找一个项目中的所有的角色的名字
        :param projectKey:  项目Key
        :return: 角色名List
        """
        project_role_dict = {}
        if self.projectIsExist(projectKey) :
            project_role_id_dict = self.getProjectRoles(projectKey)
            return list(project_role_id_dict.keys())
        else:
            return "FAIL, PROJECT IS NOT EXIST."


    def search_project_all_roles(self,projectKey):
        """
        查找一个项目中的所有角色
        :param projectKey:  项目Key
        :return:
        """
        project_role_dict = {}
        project_role_id_dict = self.getProjectRoles(projectKey)
        if project_role_id_dict is not None and len(project_role_id_dict.keys())>0:
            for rolename in project_role_id_dict.keys():
                roleid = project_role_id_dict.get(rolename).get("id")
                project_role_info = self.getProjectRoleByRoleid(projectKey,roleid)
                actors_dict_list = project_role_info.raw.get("actors")
                actors_dict_list = self.sub_pop_the_role_dict_list(actors_dict_list)

                project_role_dict[rolename] = actors_dict_list
        else:
            project_role_dict = "PROJECT ERROR"
        return project_role_dict

    def search_project_role_by_rolename(self,projectKey,rolename):
        """
        查找一个项目中的
        :param projectKey:
        :param rolename:
        :return:
        """
        if not self.projectIsExist(projectKey):
            return "FAIL, PROJECT ERROR"
        project_all_roles = self.getProjectRoles(projectKey)
        if rolename in project_all_roles.keys():
            project_role_id_info = project_all_roles.get(rolename)
            project_role_info_response = self.getProjectRoleByRoleid(projectKey,project_role_id_info.get("id"))
            project_role_actors_info = project_role_info_response.raw.get("actors")
            #project_role_info = "|".join(self.sub_pop_the_role_dict_list(project_role_actors_info))
            project_role_info = self.sub_pop_the_role_dict_list(project_role_actors_info)
            returnvalue = project_role_info
            return returnvalue
        else:
            return "FAIL, ROLE ERROR"

    def search_project_role_user(self,projectKey,rolename,username):
        """
        查找一个项目中的角色是否包含某个用户
        :param projectKey: 项目Key
        :param rolename: 角色中文名
        :param username:   用户名英文剑侠
        :return:
        """
        returnvalue = ""
        if not self.projectIsExist(projectKey):
            return "FAIL, PROJECT ERROR"
        project_all_roles = self.getProjectRoles(projectKey)
        if rolename in project_all_roles.keys():
            project_role_id_info = project_all_roles.get(rolename)
            project_role_info =  self.getProjectRoleByRoleid(projectKey,project_role_id_info.get("id")).raw.get("actors")
            project_role_info = self.sub_pop_the_role_dict_list(project_role_info)

            if len(project_role_info)>0:

                #区分批量
                if "|" in username:
                    user_input_list =username.split("|")
                    user_error_list = []
                    user_not_in_role_list = []
                    user_in_role_list = []
                    for user_single in user_input_list:
                        if not self.get_user_is_exist(user_single):
                            user_error_list.append(user_single)
                        else:
                            #用户存在
                            #轮询每个userdict，用户存在userdict则有
                            for userdict in project_role_info:
                                if "name" in userdict:
                                    if user_single in userdict.get("name"):
                                        user_in_role_list.append(user_single)
                    #user不在角色中是通过 取差集 出来的
                    user_not_in_role_list = [x for x in user_input_list if x not in user_in_role_list]

                    if len(user_error_list) == 0 and len(user_not_in_role_list)==0:
                        returnvalue = "SUCCESS"
                    else:
                        returnvalue = "FAIL, "
                        if len(user_error_list)>0:
                            returnvalue += "Users "+str(user_error_list) + " IS NOT EXIST."
                        if len(user_not_in_role_list)>0:
                            returnvalue += "Users "+str(user_not_in_role_list) + "IS NOT IN ROLE."
                else:
                    if not self.get_user_is_exist(username) :
                        return  "FAIL, User "+str(username) + " IS NOT EXIST"
                    returnvalue = "FAIL, User "+str(username) + " IS NOT IN ROLE "+str(rolename) + "."
                    for userdict in project_role_info:
                        if username in userdict.get("name"):
                            returnvalue = "SUCCESS"

            return returnvalue

        else:
            return "FAIL, ROLE ERROR"

    def search_project_role_group(self,projectKey,rolename,username):
        """
        查找一个项目中的角色是否包含某个用户
        :param projectKey: 项目Key
        :param rolename: 角色中文名
        :param username:   用户名英文剑侠
        :return:
        """
        returnvalue = ""
        if not self.projectIsExist(projectKey):
            return "FAIL, PROJECT ERROR"
        project_all_roles = self.getProjectRoles(projectKey)
        if rolename in project_all_roles.keys():
            project_role_id_info = project_all_roles.get(rolename)
            project_role_info =  self.getProjectRoleByRoleid(projectKey,project_role_id_info.get("id")).raw.get("actors")
            project_role_info = self.sub_pop_the_role_dict_list(project_role_info)

            if len(project_role_info)>0:
                for userdict in project_role_info:
                    if "name" in userdict:
                        #区分批量
                        if "|" in username:
                            user_input_list =username.split("|")
                            user_error_list = []
                            user_not_in_role_list = []
                            user_in_role_list = []
                            for user_single in user_input_list:
                                if not self.get_group_is_exist(user_single):
                                    user_error_list.append(user_single)
                                else:
                                    if user_single in userdict.get("name"):
                                        user_in_role_list.append(user_single)
                                    else:
                                        user_not_in_role_list.append(user_single)
                            if len(user_error_list) == 0 and len(user_not_in_role_list)==0:
                                returnvalue = "SUCCESS"
                            else:
                                returnvalue = "FAIL, "
                                if len(user_error_list)>0:
                                    returnvalue += "Users "+str(user_error_list) + " IS NOT EXIST."
                                if len(user_not_in_role_list)>0:
                                    returnvalue += "Users "+str(user_not_in_role_list) + "IS NOT IN ROLE."
                        else:
                            if not self.get_group_is_exist(username) :
                                return  "FAIL, User "+str(username) + " IS NOT EXIST"
                            if username in userdict.get("name"):
                                returnvalue = "SUCCESS"
            return returnvalue

        else:
            return "FAIL, ROLE ERROR"

    def add_project_role_actor(self,projectKey,rolename,actorname):
        """
        为项目角色添加用户
        :param projectKey:项目简称
        :param rolename: 角色名
        :param actorname: 用户名
        :return: SUCCESS or FAIL,+原因
        """
        returnvalue = ""
        if self.projectIsExist(projectKey):
            projectroles_dict =  self.getProjectRoles(projectKey)
            if projectroles_dict is not None:
                if rolename in projectroles_dict.keys():
                    project_role_dict  =  projectroles_dict.get(rolename)
                    project_role_id = project_role_dict.get("id")
                    #批量输入时，actorname当中带着|
                    if "|" in actorname:
                        actorlist = actorname.split("|")
                        actor_error_list = []
                        for actor_single_name in actorlist:
                            if not self.get_user_is_exist(actor_single_name):
                                actor_error_list.append(actor_single_name)
                        if len(actor_error_list)>0:
                            return "FAIL, Users "+str(actor_error_list) +" IS NOT EXIST."
                        else:
                            r = self.addProjectRoleActors(projectKey,project_role_id,actorname)
                            returnvalue =self.sub_handle_jira_return(r)
                    else:
                        if not self.get_user_is_exist(actorname):
                            return "FAIL, User "+str(actorname) +" IS NOT EXIST."
                        else:
                            r = self.addProjectRoleActor(projectKey,project_role_id,actorname)
                            returnvalue = self.sub_handle_jira_return(r)
                else:
                    returnvalue = "FAIL, ROLE ERROR"
            else:
                returnvalue = "FAIL, PROJECT ERROR"
            return returnvalue
        else:
            return "FAIL, PROJECT IS NOT EXIST"

    def add_project_role_group(self,projectKey,rolename,groupname):
        """
       为项目角色添加Group
       :param projectKey:项目简称
       :param rolename: 角色名
       :param actorname: group名
       :return: SUCCESS or FAIL,+原因
        """
        returnvalue = ""
        if self.projectIsExist(projectKey):
            projectroles_dict = self.getProjectRoles(projectKey)
            if projectroles_dict is not None:
                if rolename in projectroles_dict.keys():
                    project_role_dict = projectroles_dict.get(rolename)
                    project_role_id = project_role_dict.get("id")
                    # 批量输入时，actorname当中带着|
                    if "|" in groupname:
                        actorlist = groupname.split("|")
                        actor_error_list = []
                        for actor_single_name in actorlist:
                            if not self.get_group_is_exist(actor_single_name):
                                actor_error_list.append(actor_single_name)
                        if len(actor_error_list) > 0:
                            return "FAIL, Groups " + str(actor_error_list) + " IS NOT EXIST."
                        else:
                            r = self.addProjectRoleGroups(projectKey, project_role_id, groupname)
                            returnvalue = self.sub_handle_jira_return(r)
                    else:
                        group_is_exist =self.get_group_is_exist(groupname)
                        if not group_is_exist:
                            return "FAIL, Group " + str(groupname) + " IS NOT EXIST."
                        else:
                            r = self.addProjectRoleGroup(projectKey, project_role_id, groupname)
                            returnvalue = self.sub_handle_jira_return(r)
                else:
                    returnvalue = "FAIL, ROLE ERROR"
            else:
                returnvalue = "FAIL, PROJECT ERROR"
            return returnvalue
        else:
            return "FAIL, PROJECT IS NOT EXIST"

    def del_project_role_actor(self,projectKey,rolename,actorname):
        """
        为项目角色删除用户
        :param projectKey: 项目简称
        :param rolename: 角色中文名
        :param actorname: 预删除的用户名
        :return:
        """
        returnvalue = ""
        if not self.projectIsExist(projectKey):
            return "FAIL, PROJECT ERROR"

        projectroles_dict = self.getProjectRoles(projectKey)
        if rolename in projectroles_dict.keys():
            project_role_dict = projectroles_dict.get(rolename)
            project_role_id =  project_role_dict.get("id")
            #批量输入的情况
            if "|" in actorname:
                actors_list = actorname.split("|")
                actor_error_list =[]
                actor_not_in_role_list = []
                actor_in_role_list = []
                for actor_single_name in actors_list:
                    if not self.get_user_is_exist(actor_single_name):
                        actor_error_list.append(actor_single_name)
                    else:
                        if self.search_project_role_user(projectKey, rolename, actor_single_name) == "SUCCESS":
                            actor_in_role_list.append(actor_single_name)
                        else:
                            actor_not_in_role_list.append(actor_single_name)
                if len(actor_not_in_role_list)==0 and len(actor_error_list)==0:
                    returnvalue="SUCCESS"
                    for role_actor in actor_in_role_list:
                        self.delProjectRoleActor(projectKey,project_role_id,role_actor)

                else:
                    returnvalue = "FAIL,"
                    if len(actor_not_in_role_list)>0:
                        returnvalue += "Users "+str(actor_not_in_role_list) + "IS NOT IN ROLE "+str(rolename)+" ."
                    if len(actor_error_list)>0:
                        returnvalue += "Users "+str(actor_error_list) + "IS NOT EXIST."

            else:
                if not self.get_user_is_exist(actorname):
                    returnvalue = "FAIL, User "+ str(actorname) + " IS NOT EXIST."
                else:
                    if self.search_project_role_user(projectKey, rolename, actorname) == "SUCCESS":
                        r = self.delProjectRoleActor(projectKey,project_role_id,actorname)
                        returnvalue = self.sub_handle_jira_return(r)
                    else:
                        returnvalue = "FAIL, User "+ str(actorname) + " IS NOT IN ROLE "+str(rolename) + " ."

        else:
            returnvalue = "FAIL, ROLE ERROR"


        return returnvalue


    def del_project_role_group(self, projectKey, rolename, groupname):
        """
        为项目角色删除用户
        :param projectKey: 项目简称
        :param rolename: 角色中文名
        :param groupname: 预删除的用户名
        :return:
        """
        returnvalue = ""
        if not self.projectIsExist(projectKey):
            return "FAIL, PROJECT ERROR"

        projectroles_dict = self.getProjectRoles(projectKey)
        if rolename in projectroles_dict.keys():
            project_role_dict = projectroles_dict.get(rolename)
            project_role_id =  project_role_dict.get("id")
            #批量输入的情况
            if "|" in groupname:
                actors_list = groupname.split("|")
                actor_error_list =[]
                actor_not_in_role_list = []
                actor_in_role_list = []
                for actor_single_name in actors_list:
                    if not self.get_group_is_exist(actor_single_name):
                        actor_error_list.append(actor_single_name)
                    else:
                        if self.search_project_role_group(projectKey, rolename, actor_single_name) == "SUCCESS":
                            actor_in_role_list.append(actor_single_name)
                        else:
                            actor_not_in_role_list.append(actor_single_name)
                if len(actor_not_in_role_list)==0 and len(actor_error_list)==0:
                    returnvalue="SUCCESS"
                    for role_actor in actor_in_role_list:
                        self.delProjectRoleGroup(projectKey,project_role_id,role_actor)

                else:
                    returnvalue = "FAIL,"
                    if len(actor_not_in_role_list)>0:
                        returnvalue += "Users "+str(actor_not_in_role_list) + "IS NOT IN ROLE "+str(rolename)+" ."
                    if len(actor_error_list)>0:
                        returnvalue += "Users "+str(actor_error_list) + "IS NOT EXIST."

            else:
                if not self.get_group_is_exist(groupname):
                    returnvalue = "FAIL, User " + str(groupname) + " IS NOT EXIST."
                else:
                    if self.search_project_role_group(projectKey, rolename, groupname) == "SUCCESS":
                        r = self.delProjectRoleGroup(projectKey, project_role_id, groupname)
                        returnvalue = self.sub_handle_jira_return(r)
                    else:
                        returnvalue = "FAIL, User " + str(groupname) + " IS NOT IN ROLE " + str(rolename) + " ."

        else:
            returnvalue = "FAIL, ROLE ERROR"


        return returnvalue

    def clean_project_role(self, projectKey, rolename):
        """
        清除项目中的某个角色的所有人
        :param projectKey:项目简称
        :param rolename:角色中文名
        :return:
        """
        if not self.projectIsExist(projectKey):
            return "FAIL, PROJECT IS NOT EXIST"

        project_role_id_dict = self.getProjectRoles(projectKey)
        if project_role_id_dict is not None and len(project_role_id_dict.keys()) > 0:
            if rolename in project_role_id_dict.keys():
                roleid = project_role_id_dict.get(rolename).get("id")
                project_role_info = self.getProjectRoleByRoleid(projectKey, roleid)
                actors_dict_list = project_role_info.raw.get("actors")
                # 获得该角色内的所有的用户
                del_role_error_list= []
                for actor_info_dict in actors_dict_list:
                    if actor_info_dict.get("type") == "atlassian-group-role-actor":

                        r_result = self.del_project_role_group(projectKey,rolename,actor_info_dict.get("name"))

                        if r_result != "SUCCESS":
                            del_role_error_list.append(str(projectKey)+str(rolename)+str(actor_info_dict.get("name"))+r_result)

                    else:
                        r_result = self.del_project_role_actor(projectKey,rolename,actor_info_dict.get("name"))
                        if r_result != "SUCCESS":
                            del_role_error_list.append(
                                str(projectKey) + str(rolename) + str(actor_info_dict.get("name")) + r_result)

                if len(del_role_error_list) == 0:
                    result = "SUCCESS"
                else:
                    result = "FAIL, "+ str(del_role_error_list)

            else:
                result = "FAIL, ROLE ERROR"
        else:
            result = "FAIL, ROLE ERROR"
        return result


    def sub_pop_the_role_dict_list(self,role_dict_list):
        if len(role_dict_list) > 0:
            for actors_dict in role_dict_list:
                actors_dict.pop("type")
                actors_dict.pop("avatarUrl")
        return role_dict_list

    def sub_handle_jira_return(self,response):
        if response.ok:
            returnvalue = "SUCCESS"
        else:
            error_text = response.text
            error_message = json.loads(error_text).get("errorMessages")
            if isinstance(error_message, list):
                error_message = "".join(error_message)
            returnvalue = "FAIL," + str(error_message)
        return returnvalue
if __name__ == '__main__':
    project = "10585"
    issuetype = "准入测试问题单"
    parent = ""
    summary = "wkk测试创建问题单"
    priority = "中"
    fix_version = ""
    versions = ""
    component = "无"
    assignee = "wu.keke"
    fileds = "1.0.0"
    desc = "1.测试创建2.测试修改"

    jiraUtil = JiraUtil("wu.keke", "Dev111111@@@")
    r = jiraUtil.login()
    logger.success(f"Login result is {r}")
    start = time.time()
    by_id = jiraUtil.projectIsExist("NADDONTEST")
    print(by_id)
    # issue = jiraUtil.issue("NADDONTEST-628")
    # jql = "project='NADDONTEST'"
    #    2147483648
    # result = jiraUtil.search_issues(jql1, 150)
    # issues = jiraUtil.search_issues_limit(jql)
    end = time.time()
    # print(len(issues))
    print("执行结束,耗时=", int(round((end - start))), "s")

    # print(result['status'])
    # print(len(result['result']))
    # print(issue.fields)
    #
    # print("问题单id: ", issue.id)
    # print("问题单key: ", issue.key)
    # print("主题: ", issue.fields.summary)
    # print("类型: ", issue.fields.issuetype)
    # print("经办人 ", issue.fields.assignee)
    # print("描述: ", issue.fields.description)
    # print("优先级: ", issue.fields.priority)
    # print("项目: ", issue.fields.project)
    # print("项目名: ", issue.fields.project.name)
    # print("项目key: ", issue.fields.project.key)
    # print("项目id: ", issue.fields.project.id)
    # print("----: ", issue.fields.customfield_10706)
    # print("--------------------------------------------------")
    # jiraUtil.create_issue(project, issuetype, parent, summary, priority
    #                       , fix_version, versions, component, assignee, fileds, desc)
    # update_assignee = jiraUtil.updateAssignee("NADDONTEST-628", 'wu.keke')
    # print(update_assignee)

    # issue_dict = {
    #         'issuetype': {'name': issuetype},  # 问题类型
    #         'summary': "WKK测试修改",  # 问题主题
    #         'priority': {'name': "高"},  # 优先级
    #         'description': "测试修改",  # 问题描述
    #
    #     }
    # jiraUtil.update_issue(issue,issue_dict)
