import sys
import re

"""
正则相关的基础库
"""
class RegUtil(object):
    def __init__(self):
        pass

    def reg_image_version(self,version):
        """
        镜像有关的版本号正则
        版本号两头为数字字母，仅兼容_-.符号，且不能出现任意两个符号连续的场景
        :param version:  输入的待校验的的
        :return: 是否符合规则
        """
        regex_result = False
        #1.版本号由数字字母及_-.符号构成,版本号的首尾为数字或字母
        regex_pattern1 = r"^[0-9a-zA-Z]+[\-\_\.0-9a-zA-Z]*[0-9a-zA-Z]$"
        match_result1 = re.match(regex_pattern1,version)
        #2.版本号中的字符不能连续
        regex_pattern2 = r"^.*((\-\_)|(\-\.)|(\-\-)|(\_\-)|(\_\.)|(\_\_)|(\.\-)|(\.\_)|(\.\.)).*$"
        match_result2 = re.match(regex_pattern2,version)

        if match_result1 is not None :
            if match_result2 is not None:
                regex_result = False
            else:
                regex_result = True
        else:
            regex_result = False

        return regex_result


if __name__ == '__main__':
    version_input = "ab.5j.a3k"
    regutil = RegUtil()
    reg_result = regutil.reg_image_version(version_input)
    print(str(reg_result))




