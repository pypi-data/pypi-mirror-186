# -*- coding:UTF-8 -*-
"""
__title__ = ''
__author__ = 'wu.keke'
__mtime__ = '2020/4/14'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.

os基础库 - win32文件与文件夹部分
1.windows 下判断路径是否存在
2.windows 下判断路径是文件或是文件夹
3.windows 下判断文件属性（隐藏或非隐藏）
4.windows 下拷贝文件
5.windows 下递归拷贝文件夹
6.windows 下生成文件 md5
7.isdir   是否是目录
8.copyDir  全量拷贝
9.copyDir_Ignore_hidden   默认忽略隐藏的文件或者文件夹
10.copyDir_Ignore_custom   自定义忽略文件['','','等等']
11.copytree   shutil.copytree()shutil自带的拷贝以及过滤,不好用,容易报错,目标文件夹存在的时候报错,需要先删除同名目标文件夹,不安全
12.生成文件名字
"""
import hashlib
import os
import re
import shutil
import traceback
import win32api

import win32con
import locale
#from loguru import logger
from halring.log.loguru_util import LoguruUtil

import chardet
import sys
import subprocess
import stat

logger = LoguruUtil()

# noinspection PyShadowingBuiltins
class OsUtil:
    def __init__(self):
        pass


    def exists(self, path):
        """
        function used for judge whether the file exists
        :__Author__ : wu.keke
        :__mtime__ : 2020/4/14 17:59

        :param path: file path or dir
        :return: true or false

        """

        return os.path.exists(path)

    def isfile(self, path):
        """
        function used for judge whether is a document
        :__Author__ : wu.keke
        :__mtime__ : 2020/4/14 17:59

        :param path: file path or dir
        :return: true or false

        """

        return os.path.isfile(path)

    def isdir(self, path):
        """
        function used for judge whether is a dir
        :__Author__ : wu.keke
        :__mtime__ : 2020/4/14 17:59

        :param path: file path or dir
        :return: true or false

        """

        return os.path.isdir(path)

    def isHidden(self, path):
        """
        function used for judge file attribute
        :__Author__ : wu.keke
        :__mtime__ : 2020/4/14 17:59

        is hidden return true or return false

        :param path: file path or dir
        :return: true or false

        """

        if self.exists(path):
            attr = win32api.GetFileAttributes(path)
            if attr & win32con.FILE_ATTRIBUTE_HIDDEN:
                return True
            else:
                return False
        else:
            logger.error(f"{path} 文件不存在!")
            return False

    def copyFile(self, fromPath, toPath):
        """
        function used for copy file
        :__Author__ : wu.keke
        :__mtime__ : 2020/4/14 17:59

        :param fromPath: file  srcpath
        :param toPath: file dstpath
        :return: true or false

        """
        try:
            if self.isfile(fromPath):
                shutil.copy(fromPath, toPath)
                return True
            else:
                logger.error(f"{fromPath} 不是一个文件!")
                return False
        except Exception as ex:
            logger.error("\tError %s\n" % ex)
            logger.error(traceback.format_exc())
            return False

    def copyDir(self, srcDir, dstDir):
        """
        全量拷贝
        function used for copy dir
        :__Author__ : wu.keke
        :__mtime__ : 2020/4/14 17:59

        :param srcDir: src dir
        :param dstDir: dst dir
        :return: true or false

        """
        try:
            if self.exists(srcDir):
                if not self.isfile(srcDir) and not self.isfile(dstDir):
                    if not self.exists(dstDir):
                        os.mkdir(dstDir)

                    files = os.listdir(srcDir)
                    for file in files:
                        srcname = os.path.join(srcDir, file)
                        dstname = os.path.join(dstDir, file)
                        if os.path.isdir(srcname):
                            self.copyDir(srcname, dstname)
                        else:
                            self.copyFile(srcname, dstname)

                    return True
                else:
                    logger.error(f"{srcDir} or {dstDir} 不是目录,请检查!")
                    return False
            else:
                logger.error(f"{srcDir} 目录不存在!")
                return False
        except Exception as ex:
            logger.error("\tError %s\n" % ex)
            logger.error(traceback.format_exc())
            return False

    def copyDir_ignore_hidden(self, srcDir, dstDir):
        """
        默认不拷贝隐藏的文件,此方法和copyDir可以合并,为方便调用单独列出
        function used for copy dir
        :__Author__ : wu.keke
        :__mtime__ : 2020/4/14 17:59

        :param srcDir: src dir
        :param dstDir: dst dir
        :return: true or false

        """
        try:
            if self.exists(srcDir):
                if not self.isfile(srcDir) and not self.isfile(dstDir):
                    if not self.exists(dstDir):
                        os.mkdir(dstDir)

                    files = os.listdir(srcDir)
                    for file in files:
                        srcname = os.path.join(srcDir, file)
                        dstname = os.path.join(dstDir, file)
                        if os.path.isdir(srcname) and not self.isHidden(srcname):
                            self.copyDir_ignore_hidden(srcname, dstname)
                        else:
                            if not self.isHidden(srcname):
                                self.copyFile(srcname, dstname)

                    return True
                else:
                    logger.error(f"{srcDir} or {dstDir} 不是目录,请检查!")
                    return False
            else:
                logger.error(f"{srcDir} 目录不存在!")
                return False
        except Exception as ex:
            logger.error("\tError %s\n" % ex)
            logger.error(traceback.format_exc())
            return False

    def copyDir_ignore_custom(self, srcDir, dstDir, ignore_pattern):
        """
        ignore_pattern=["dir1","test.txt"]
        自定义过滤不需要拷贝的文件夹或文件
        此处为方便调用.过滤条件只需提供名称,若有需求指定某个文件夹下的某个名称不拷贝,后续再定制开发

        function used for copy dir
        :__Author__ : wu.keke
        :__mtime__ : 2020/4/14 17:59

        :param srcDir: src dir
        :param dstDir: dst dir
        :return: true or false

        """
        try:
            if self.exists(srcDir):
                if not self.isfile(srcDir) and not self.isfile(dstDir):
                    if not self.exists(dstDir):
                        os.mkdir(dstDir)

                    files = os.listdir(srcDir)
                    for file in files:
                        srcname = os.path.join(srcDir, file)
                        dstname = os.path.join(dstDir, file)
                        if file not in ignore_pattern:
                            if os.path.isdir(srcname):
                                self.copyDir_ignore_custom(srcname, dstname)
                            else:
                                self.copyFile(srcname, dstname)
                    return True
                else:
                    logger.error(f"{srcDir} or {dstDir} 不是目录,请检查!")
                    return False
            else:
                logger.error(f"{srcDir} 目录不存在!")
                return False
        except Exception as ex:
            logger.error("\tError %s\n" % ex)
            logger.error(traceback.format_exc())
            return False

    def copytree(self, src, tar, ingore_pattern):
        """
        shutil自带的copytree不是很好用,在已有目标文件夹的时候会报错,建议使用copyDir 系列方法
        此处 ingore_pattern  暂只支持一个字符窜,如需多个,可直接使用
        shutil.copytree(src, tar, ignore=shutil.ignore_patterns("1.txt","2.txt","等等"))
        :param src:
        :param tar:
        :param ingore_pattern: None or str
        :return:
        """
        ingore_pattern = ingore_pattern if ingore_pattern is not None else ""
        shutil.copytree(src, tar, ignore=shutil.ignore_patterns(ingore_pattern))
        return True

    def get_file_md5(self, file_path):
        """
        function used for get md5
        :__Author__ : wu.keke
        :__mtime__ : 2020/4/14 17:59

        :param file_path: path,txt zip...
        :return: md5

        """
        if self.exists(file_path) & self.isfile(file_path):

            with open(file_path, 'rb')as f:
                md5obj = hashlib.md5()
                md5obj.update(f.read())
                _hash = md5obj.hexdigest()

            return str(_hash).upper()
        else:
            logger.error(f"{file_path} 文件不存在! or 路径不是文件")
            return None

    def mkdir(self, dirName):
        """
        :param dirName: 要创建的路径,创建单个目录
        :return:
        """
        try:
            if self.exists(dirName):
                return True
            else:
                os.mkdir(dirName)
        except Exception as ex:
            logger.error('该函数只能创建单个目录')
            logger.error(traceback.format_exc())
            return False
        return True

    def mkdirs(self, dirName):
        """
        :param dirName: 要创建的路径,创建多级目录
        :return:
        """
        try:
            if self.exists(dirName):
                return True
            else:
                os.makedirs(dirName)
        except Exception as ex:
            logger.error(traceback.format_exc())
            return False
        return True

    def removeDirs(self, dirName, isDeleteOuterMostDir=None):
        """
        递归删除目录下所有内容,默认不删除最外层目录,靠 isDeleteOuterMostDir判断是否删除最外层文件夹
        :param dirName:
        :param isDeleteOuterMostDir: True时删除最外层目录,不传或False不删除最外层
        :return:
        """
        try:
            if not self.exists(dirName):
                return True
            else:
                if self.isdir(dirName):
                    files = os.listdir(dirName)
                    for file in files:
                        srcname = os.path.join(dirName, file)
                        os.chmod(srcname, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
                        if os.path.isdir(srcname):
                            self.removeDirs(srcname)
                            os.rmdir(srcname)
                        else:
                            os.remove(srcname)

                    if isDeleteOuterMostDir is not None and isDeleteOuterMostDir is True:
                        os.removedirs(dirName)
        except Exception as ex:
            logger.error(traceback.format_exc())
            return False
        return True

    def unionPath(self, path, *paths):
        """
        :param path: 第一个路径参数
        :param paths: 无限拼接  一般只是名字的字符串即可,不用带 \\ or /
        :return: newPath
        """

        return os.path.join(path, *paths)

    def listFile(self, dir):
        """
        递归遍历目录下所有目录以及文件,返回的是路径格式字符串
        :param dir: dir
        :return: list
        """
        list = []
        self.getFileList(dir, list)
        return list

    def getFileList(self, dir, list):
        """
        递归遍历目录下所有目录以及文件子方法,系统调用,用户不需要调用
        :param dir:
        :param list:
        :return:
        """
        if self.isdir(dir) and self.exists(dir):
            listdir = os.listdir(dir)
            if len(listdir) == 0:
                list.append(dir)
            else:
                for fname in listdir:
                    np = os.path.join(dir, fname)
                    if self.isdir(np):
                        self.getFileList(np, list)

                    else:
                        list.append(os.path.join(dir, fname))
        else:
            logger.error(f'{dir} 不存在或者不是一个目录!')
            return list

    # def unicodeToUtf8(self, strs):
    #     """
    #
    #     :param strs: 传入的字符串
    #     :return:
    #     """
    #     of_str = osutil.typeOfStr(strs)
    #     if str(of_str) == "<class 'bytes'>":
    #         return str(strs).encode('utf-8')
    #     else:
    #         return strs.encode('utf-8')

    def typeOfStr(self, init_str):
        """
        判断字符串类型
        :param init_str: 传入的字符串
        :return:
        """

        return type(init_str)

    def encodeType(self, init_str):
        """
        判断字符串编码

        :param init_str: 传入的字符串
        :return:
        """
        of_str = osutil.typeOfStr(init_str)
        if str(of_str) == "<class 'bytes'>":
            return chardet.detect(str.encode(str(init_str)))['encoding']
        else:
            return chardet.detect(str.encode(init_str))['encoding']

    def popen_no_block(self, command):
        """
         win cmd命令返回输出结果  非阻塞式
        :param command: cmd命令
        :return: str
        """
        # 若有编码问题错误,打开此处试下
        # try:
        cmd = os.popen(command)
        a = cmd.buffer.read()
        data = a.decode(encoding='gbk')
        # except UnicodeDecodeError as e:
        #     if "gbk" in e.args:
        #         cmd = os.popen(command)
        #         data = cmd.buffer.read().decode(encoding='cp936')
        # data=cmd.buffer.read().decode(encoding='gbk')
        # data = cmd.read()
        cmd.close()
        return data

    def popen_block(self, svn_export_cmd):

        """
        阻塞式执行命令
        :param svn_export_cmd: cmd
        :return:
        """
        stdout = subprocess.Popen(svn_export_cmd, stdout=subprocess.PIPE, shell=True)
        # p_status = p.communicate()
        return stdout

    def popen_block2(self, cmd):
        """
        
        :param cmd:
        :return:
        """
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout = p.stdout.read()
        stderr = p.stderr.read()
        p.communicate()
        if p.returncode == 0:
            return {"status": True,
                    "rc": p.returncode,
                    "message": stdout}
        else:
            return {"status": False,
                    "rc": p.returncode,
                    "message": stderr}
            # return p.stdout


    # noinspection PyIncorrectDocstring
    def check_rename(self, filePath, splitStr="-"):
        """
        给出一个本地文件路径，返回自增的文件名(不带目录路径)
        Args:
            filePath:文件全路径 for example: D:\\2020\\test\\test.txt
            splitStr:文件名称分割符 for example: test-1.txt  '-'就是分隔符,默认为-
        Returns:
            自增的文件名
        """
        dirName = os.path.dirname(filePath)
        fileName = os.path.basename(filePath)
        name_ = os.path.splitext(fileName)[0]
        type_ = os.path.splitext(fileName)[1]

        baseName = name_
        maxNumber = 1

        if self.isdir(dirName):
            listdir = os.listdir(dirName)
            for fname in listdir:
                _name_ = os.path.splitext(fname)[0]
                nameMap = self.__getNameDict(_name_, splitStr)
                if name_ == nameMap["basename"]:
                    baseName = nameMap["basename"]
                    maxNumber = int(nameMap["num"]) + 1

            newName = baseName + splitStr + str(maxNumber) + type_
            return newName
        else:
            logger.error(f"{dirName} 不是目录")
            return ''

    def __getNameDict(self, name_, splitStr="-"):

        nameMap = {}
        # 命名分隔符默认为"-",则将最后一次出现分割符号以及之后的字符串全部去掉,只需要基础名称
        name_pretext = name_.rpartition(splitStr)[0]
        number_suffixtext = name_.rpartition(splitStr)[2]

        base_name = name_pretext if name_pretext else name_

        if number_suffixtext.isnumeric():
            # number_suffix只保留末两位
            number_suffix = int(number_suffixtext)
            number_suffixtext = str(number_suffix)[-2:]
        else:
            base_name = name_
            number_suffixtext = "0"

        # if len(baseName.strip()) == 0:
        #     num = "0"
        # else:
        #     num = name_[name_.rfind(splitStr):len(name_)].replace("_", "")

        # else:
        #     #     若没有命名分隔符,则仅去除序号数字,保留基础字符串为基础名称
        #     name_.rpartition()
        #     baseName = "".join((name_[:name_.rfind("\D")], "", name_[len(name_):]))
        #     if len(baseName.strip()) == 0:
        #         baseName = name_
        #         num = "0"
        #     else:
        #         num = name_[name_.rfind("\D"):len(name_)]

        nameMap["basename"] = base_name
        nameMap["num"] = number_suffixtext
        return nameMap

    def get_cmd_encode_type(self):

        # 获取当前cmd窗口的字符编码，通常为936(GBK)
        chcp_result = self.popen_block2("chcp").get("message")
        encode_type = re.split(b'[:]',chcp_result)[-1].strip().decode("UTF-8")
        return encode_type

if __name__ == '__main__':
    f_path = "\\\\196.131.1.78\\temp\\personal\\wukeke\\问题还原版本\\2.5.5\\用户中心-外部认证服务2.5.5对外影响分析.docx"
    topath = "D:\\2020\\test\\a.txt"
    osutil = OsUtil()
    # popen = osutil.popen("start D:\\tools\\EditPlus\\EditPlus.exe")
    name = osutil.popen_no_block("dir")
    print(name)

    # input = ['asdad23', '26asfdsa90', 'sdaj_89']
    #
    # for s in input:
    #     print(re.sub(".*?([0-9]*)$",s))
