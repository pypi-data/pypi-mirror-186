# coding=utf-8
import requests
from halring.log.loguru_util import logger


class RequestUtil:
    """
    :author
        zqxu
    :param

    :param

    :param

    :return:
    """
    @staticmethod
    def get_token(username, password):
        url = "http://10.112.6.7:8080/api/user/login"
        login_data = {
            "domainAccount": username,
            "password": password
        }
        login_rslt = RequestUtil()
        r = login_rslt.post(url, json=login_data)
        return r.json()["message"]["token"]

    @staticmethod
    def get_download_key(username, password):
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        key_rslt = RequestUtil()
        headers["Authorization"] = key_rslt.get_token(username=username, password=password)
        url = "http://10.112.6.93:9527/api/file/nextSerialNo"
        get_data = {

        }
        r = key_rslt.get(url, get_data, headers=headers)
        return r.json()["message"]

    @staticmethod
    def get(url, data=None, headers=None, **kwargs):
        """
        使用get方法提交
        :param headers:
        :param url:
        :param data:
        :param kwargs:
        :return:
        """
        try:
            res = requests.get(url, params=data, headers=headers, **kwargs)
        except Exception as e:
            logger.error(str(e))
        else:
            return res

    @staticmethod
    def put(url, data=None, headers=None, **kwargs):
        """
        使用put方法提交
        :param headers:
        :param url:
        :param data:
        :param kwargs:
        :return:
        """
        try:
            res = requests.put(url, params=data, headers=headers, **kwargs)
        except Exception as e:
            logger.error(str(e))
        else:
            return res

    @staticmethod
    def delete(url, data=None, headers=None, **kwargs):
        """
        使用delete方法提交
        :param headers:
        :param url:
        :param data:
        :param kwargs:
        :return:
        """
        try:
            res = requests.delete(url, params=data, headers=headers, **kwargs)
        except Exception as e:
            logger.error(str(e))
        else:
            return res

    @staticmethod
    def post(url, data=None, json=None, headers=None, **kwargs):
        """
        使用post方法提交
        :param headers:
        :param json:
        :param url:
        :param data:
        :param kwargs:
        :return:
        """
        try:
            res = requests.post(url, data=data, json=json, headers=headers, **kwargs)
        except Exception as e:
            logger.error(str(e))
        else:
            return res

    def visit(self, method, url, params=None, data=None, json=None, **kwargs):
        """
        通用方法，通过参数method选择post/get方法
        :param json:
        :param method:
        :param url:
        :param params:
        :param data:
        :param kwargs:
        :return:
        """
        if method == 'get':
            return self.get(url, data=params, **kwargs)
        elif method == 'post':
            return self.post(url, data=data, json=json, **kwargs)
        else:
            return requests.request(method, url, **kwargs)

    def rslt2json(self, method, url, params=None, data=None, json=None, **kwargs):
        """
        将返回的报文结果转换成json格式
        :param json:
        :param method:
        :param url:
        :param params:
        :param data:
        :param kwargs:
        :return:
        """
        res = self.visit(method, url, params=params, data=data, json=json, **kwargs)
        try:
            return res.json()
        except TypeError as e:
            logger.error("不是json格式数据 " + str(e))

    def rslt2dict(self, method, url, params=None, data=None, json=None, **kwargs):
        """
        将返回的报文结果转换成dict格式
        :param json:
        :param method:
        :param url:
        :param params:
        :param data:
        :param kwargs:
        :return:
        """
        res = self.visit(method, url, params=params, data=data, json=json, **kwargs)
        try:
            return res.__dict__
        except TypeError as e:
            logger.error("不是dict格式数据 " + str(e))

    def rslt2module(self, method, url, params=None, data=None, json=None, **kwargs):
        """
        将返回的报文结果转换成module格式
        :param json:
        :param method:
        :param url:
        :param params:
        :param data:
        :param kwargs:
        :return:
        """
        res = self.visit(method, url, params=params, data=data, json=json, **kwargs)
        try:
            return res.__module__
        except TypeError as e:
            logger.error("不是module格式数据 " + str(e))


if __name__ == '__main__':
    turl = "http://127.0.0.1:8000/login/"
    post_data = {
        'domainAccount': 'admin',
        'password': '123456'
    }
    rslt = RequestUtil()
    t = rslt.post(turl, post_data)
    print(t.text)
