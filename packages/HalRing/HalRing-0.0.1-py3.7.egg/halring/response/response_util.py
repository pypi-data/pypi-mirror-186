# -*- coding:UTF-8
"""
__title__ = ''
__author__ = 'rzzhou'
__mtime__ = '2021/1/22'
#我吉良吉影只想过平静的生活
Response 基础库
"""

import json

class ResponseUtil:
    def response_restapi_status_data(self, request_response):
        """
        处理http方法的的response,输出状态与数据
        :param request_response: http返回
        :return:
            {"status":"","data":""}
        """
        try:
            response_status = request_response.raw.status
            if request_response.text is not None and request_response.text != '':
                response_data = json.loads(request_response.text)  # 用json.loads转化为python的数据对象
            else:
                response_data = None

            if str(response_status) == "200":
                # 成功
                return_dict_status = True
            else:
                # 成功以外的状态
                return_dict_status = False
            returndict = {"status": return_dict_status, "data": response_data}
            return returndict
        except Exception as e:
            print(e)
