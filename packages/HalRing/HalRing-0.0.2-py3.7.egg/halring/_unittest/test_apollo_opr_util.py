# -*- coding:UTF-8 -*-
"""
__title__ = 'test_apollo_opr_util'
__author__ = 'rzzhou'
__mtime__ = '2021/01/18'
#我吉良吉影只想过平静的生活
"""
import unittest

from halring.apollo.apollo_opr_util import ApolloOprUtil

from halring.response.response_util import ResponseUtil

class TestApolloOprUtil(unittest.TestCase):
    def test_apollo_opr_util_001_get_apps(self):
        apollo_util = ApolloOprUtil("http://10.112.15.114:8070", "d8dc068f684cd0c630deb1f902fef8fddb6bdf0b", "aqc001")
        request_response = apollo_util.get_apps()
        get_app_result =ResponseUtil().response_restapi_status_data(request_response)
        print(str(get_app_result))

        assert get_app_result.get("status")

    def test_apollo_opr_util_002_get_app_lantern_control(self):
        apollo_util = ApolloOprUtil("http://10.112.15.114:8070", "d8dc068f684cd0c630deb1f902fef8fddb6bdf0b", "aqc001")
        appid="lantern-control"
        request_response = apollo_util.get_apps(appid)
        get_app_result = ResponseUtil().response_restapi_status_data(request_response)
        print(str(get_app_result))
        assert get_app_result.get("status")

    def test_apollo_opr_util_003_get_appid_env_clusters(self):
        apollo_util = ApolloOprUtil("http://10.112.15.114:8070", "d8dc068f684cd0c630deb1f902fef8fddb6bdf0b", "aqc001")
        get_result = apollo_util.get_appid_env_clusters("lantern-control")
        print(str(get_result))
        assert get_result=={'status': True, 'value': [{'env': 'DEV', 'clusters': ['default']}]}

    def test_apollo_opr_util_004_check_appid_env_is_exist(self):
        apollo_util = ApolloOprUtil("http://10.112.15.114:8070", "d8dc068f684cd0c630deb1f902fef8fddb6bdf0b", "aqc001")
        check_result = apollo_util.check_appid_env_exist("lantern-control","DEV")
        print(str(check_result))
        assert check_result

    def test_apollo_opr_util_005_check_appid_env_not_exist(self):
        apollo_util = ApolloOprUtil("http://10.112.15.114:8070", "d8dc068f684cd0c630deb1f902fef8fddb6bdf0b", "aqc001")
        check_result = apollo_util.check_appid_env_exist("lantern-control","PROD")
        print(str(check_result))
        assert not check_result

    def test_apollo_opr_util_006_check_appid_env_not_exist(self):
        apollo_util = ApolloOprUtil("http://10.112.15.114:8070", "d8dc068f684cd0c630deb1f902fef8fddb6bdf0b", "aqc001")
        check_result = apollo_util.check_appid_env_exist("lantern-not-exist","PROD")
        print(str(check_result))
        assert not check_result


    def test_apollo_opr_util_007_check_appid_env_cluster_is_exist(self):
        apollo_util = ApolloOprUtil("http://10.112.15.114:8070", "d8dc068f684cd0c630deb1f902fef8fddb6bdf0b", "aqc001")
        check_result = apollo_util.check_appid_env_cluster_exist("lantern-control","DEV","default")
        print(str(check_result))
        assert check_result

    def test_apollo_opr_util_008_check_appid_env_cluster_is_not_exist(self):
        apollo_util = ApolloOprUtil("http://10.112.15.114:8070", "d8dc068f684cd0c630deb1f902fef8fddb6bdf0b", "aqc001")
        check_result = apollo_util.check_appid_env_cluster_exist("lantern-control","PROD","default")
        print(str(check_result))
        assert not check_result

    def test_apollo_opr_util_009_check_appid_env_cluster_namespace_is_exist(self):
        apollo_util = ApolloOprUtil("http://10.112.15.114:8070", "d8dc068f684cd0c630deb1f902fef8fddb6bdf0b", "aqc001")
        check_result = apollo_util.check_appid_env_cluster_namespace_exist("lantern-control", "DEV", "default","application")
        print(str(check_result))
        assert check_result

    def test_apollo_opr_util_010_check_appid_env_cluster_namespace_not_exist(self):
        apollo_util = ApolloOprUtil("http://10.112.15.114:8070", "d8dc068f684cd0c630deb1f902fef8fddb6bdf0b", "aqc001")
        check_result = apollo_util.check_appid_env_cluster_namespace_exist("lantern-not-exist", "DEV", "default","application")
        print(str(check_result))
        assert not check_result

    def test_apollo_opr_util_011_get_appid_cluster_namespace_001_success(self):
        apollo_util = ApolloOprUtil("http://10.112.15.114:8070", "d8dc068f684cd0c630deb1f902fef8fddb6bdf0b", "aqc001")
        appid = "lantern-control"
        env = "DEV"
        cluster = "default"
        request_response = apollo_util.get_appid_env_cluster_namespace(appid,env,cluster)
        get_result = ResponseUtil().response_restapi_status_data(request_response)
        print(str(get_result))
        assert get_result.get("status")

    def test_apollo_opr_util_012_get_appid_cluster_namespace_002_failure(self):
        apollo_util = ApolloOprUtil("http://10.112.15.114:8070", "d8dc068f684cd0c630deb1f902fef8fddb6bdf0b", "aqc001")
        appid = "lantern-control"
        env = "DEV"
        cluster = "not exist"
        request_response = apollo_util.get_appid_env_cluster_namespace(appid,env,cluster)
        get_result = ResponseUtil().response_restapi_status_data(request_response)
        print(str(get_result))
        assert not get_result.get("status")

    def test_apollo_opr_util_013_get_appid_cluster_namespace_003_success_all(self):
        apollo_util = ApolloOprUtil("http://10.112.15.114:8070", "d8dc068f684cd0c630deb1f902fef8fddb6bdf0b", "aqc001")
        appid = "lantern-control"
        env = "DEV"
        cluster = "default"
        namespace = "application"
        request_response = apollo_util.get_appid_env_cluster_namespace(appid,env,cluster,namespace)
        get_result = ResponseUtil().response_restapi_status_data(request_response)
        print(str(get_result))
        assert get_result.get("status")


    def test_apollo_opr_util_014_get_appid_namespace_item_success(self):
        apollo_util = ApolloOprUtil("http://10.112.15.114:8070", "d8dc068f684cd0c630deb1f902fef8fddb6bdf0b", "aqc001")
        appid = "lantern-control"
        env = "DEV"
        cluster = "default"
        namespace = "application"
        item_key = "lantern_jira_server"
        request_response = apollo_util.get_appid_namespace_item(appid,env,cluster,namespace,item_key)
        get_result = ResponseUtil().response_restapi_status_data(request_response)
        print(str(get_result))

    def test_apollo_opr_util_015_get_appid_namespace_item_fail(self):
        apollo_util = ApolloOprUtil("http://10.112.15.114:8070", "d8dc068f684cd0c630deb1f902fef8fddb6bdf0b", "aqc001")
        appid = "lantern-control"
        env = "DEV"
        cluster = "default"
        namespace = "application"
        item_key = "lantern_item_not_exist"
        request_response = apollo_util.get_appid_namespace_item(appid,env,cluster,namespace,item_key)
        get_result = ResponseUtil().response_restapi_status_data(request_response)
        print(str(get_result))
        assert not get_result.get("status")

    def test_apollo_opr_util_016_add_appid_namespace_item_success(self):
        apollo_util = ApolloOprUtil("http://10.112.15.114:8070", "d8dc068f684cd0c630deb1f902fef8fddb6bdf0b", "aqc001")
        appid = "lantern-control"
        env = "DEV"
        cluster = "default"
        namespace = "application"
        item_key = "lantern_new_item_key"
        item_value = "lantern_new_item_value"

        post_result = apollo_util.add_appid_namespace_item(appid,env,cluster,namespace,item_key,item_value)
        add_result = ResponseUtil().response_restapi_status_data(post_result)
        print(str(add_result))
        exist = apollo_util.check_appid_namespace_item_exist(appid,env,cluster,namespace,item_key)
        print(str(exist))
        if exist:
            del_response = apollo_util.delete_appid_namespace_item(appid,env,cluster,namespace,item_key)
            del_result = ResponseUtil().response_restapi_status_data(del_response)
            print(str(del_result))

    def test_apollo_opr_util_017_del_appid_namespace_item_success(self):
        apollo_util = ApolloOprUtil("http://10.112.15.114:8070", "d8dc068f684cd0c630deb1f902fef8fddb6bdf0b", "aqc001")
        appid = "lantern-control"
        env = "DEV"
        cluster = "default"
        namespace = "application"
        item_key = "lantern_new_item_key"
        item_value = "lantern_new_item_value"

        # add_result = apollo_util.add_appid_namespace_item(appid,env,cluster,namespace,item_key,item_value)
        # print(str(add_result))
        exist = apollo_util.check_appid_namespace_item_exist(appid,env,cluster,namespace,item_key)
        print(str(exist))
        if exist:
            del_response = apollo_util.delete_appid_namespace_item(appid,env,cluster,namespace,item_key)
            del_result= ResponseUtil().response_restapi_status_data(del_response)
            print(str(del_result))

    def test_apollo_opr_util_018_release_appid_namespace_success(self):
        apollo_util = ApolloOprUtil("http://10.112.15.114:8070", "d8dc068f684cd0c630deb1f902fef8fddb6bdf0b", "aqc001")
        appid = "lantern-control"
        env = "DEV"
        cluster = "default"
        namespace = "application"
        release_title = "api_release_20210120"

        # add_result = apollo_util.add_appid_namespace_item(appid,env,cluster,namespace,item_key,item_value)
        # print(str(add_result))
        re_response = apollo_util.release_apppid_namespace(appid,env,cluster,namespace,release_title)
        re_result =ResponseUtil().response_restapi_status_data(re_response)
        print(str(re_result))

    def test_apollo_opr_util_019_export_appid_namespace_success(self):
        apollo_util = ApolloOprUtil("http://10.112.15.114:8070", "d8dc068f684cd0c630deb1f902fef8fddb6bdf0b", "aqc001")
        appid = "lantern-control"
        env = "DEV"
        cluster = "default"
        namespace = "application"

        result = apollo_util.export_appid_namespace(appid,env,cluster,namespace)
        print(str(result))
        assert result


    def test_apollo_opr_util_020_import_appid_namespace_success(self):
        apollo_util = ApolloOprUtil("http://10.112.15.114:8070", "d8dc068f684cd0c630deb1f902fef8fddb6bdf0b", "aqc001")
        appid = "lantern-control"
        env = "DEV"
        cluster = "default"
        namespace = "application"
        reset = True
        input_dict = {
            "lantern_jira_server":"http://eqops.tc.com/jira/",
            "lantern_jira_user":"pzgl",
            "lantern_jira_password":"Lantern@2020",
            "lantern_jira_db":"10.112.6.209",
            "lantern_git":"NGAir"

        }
        import_result = apollo_util.import_appid_namespace(appid,env,cluster,namespace,input_dict,reset)
        print(str(import_result))

    def test_apollo_opr_util_021_export_latet_released_appid_namespace_success(self):
        apollo_util = ApolloOprUtil("http://10.112.15.114:8070", "d8dc068f684cd0c630deb1f902fef8fddb6bdf0b",
                                    "aqc001")
        appid = "lantern-control"
        env = "DEV"
        cluster = "default"
        namespace = "application"

        result = apollo_util.export_latest_released_appid_namespace(appid, env, cluster, namespace)
        print(str(result))
        assert result

