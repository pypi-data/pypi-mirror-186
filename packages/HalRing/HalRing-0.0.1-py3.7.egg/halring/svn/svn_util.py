# -*- coding:UTF-8 -*-
import operator
import os
import re
from collections import Counter
from halring.windows import OsUtil

# nga_root = os.path.abspath(__file__).split("utils")[0]


class SvnUtil(object):

    def __init__(self, username, password):
        """
        基础信息
        Author: Chenying
        :param username: 账号
        :param password: 密码
        """
        self._username = username
        self._password = password

    def svn_info(self, remote_path):
        """
        获得详细信息
        Author: Chenying
        :param remote_path: 远端路径
        :return: 信息dict|IS_NOT_EXIST
        """
        # SVN INFO命令，路径、用户名、密码
        svn_info_cmd = 'svn info ' + remote_path + ' --username ' + self._username + ' --password ' + self._password
        # 执行SVN INFO命令,逐行读取SVN INFO命令输出字符串
        run_cmd = OsUtil().popen_no_block(svn_info_cmd)
        # 返回一个包含各行字符串作为元素的列表
        info_splitlines_list = run_cmd.splitlines()

        return 'IS_NOT_EXIST' if not info_splitlines_list else dict(
            [info_lines.split(': ') for info_lines in info_splitlines_list if not re.match(info_lines, ': ')])

    def svn_info_get_revision(self, remote_path):
        """
        获取REVISION
        :param remote_path: 远端路径
        :return: REVISION|IS_NOT_EXIST
        """
        if self.svn_info(remote_path) == 'IS_NOT_EXIST':
            return 'IS_NOT_EXIST'
        else:
            # 获取路径详细信息
            return self.svn_info(remote_path)['Revision']

    def svn_info_get_commit_id(self, remote_path):
        """
        获取COMMIT_ID
        :param remote_path: 远端路径
        :return: COMMIT_ID|IS_NOT_EXIST
        """
        if self.svn_info(remote_path) == 'IS_NOT_EXIST':
            return 'IS_NOT_EXIST'
        else:
            # 获取路径详细信息
            return self.svn_info(remote_path)['Last Changed Rev']

    def svn_info_is_file_or_directory(self, remote_path):
        """
        判断文件or文件夹
        Author: Chenying
        :param remote_path: 远端路径
        :return: IS_FILE_EXIST|IS_DIRECTORY_EXIST|IS_NOT_EXIST
        """

        if self.svn_info(remote_path) == 'IS_NOT_EXIST':
            return 'IS_NOT_EXIST'
        else:
            # 获取路径详细信息
            info_dict = self.svn_info(remote_path)['Node Kind']
            # 判断远端路径的类型：IS_NOT_EXIST|IS_FILE_EXIST|IS_DIRECTORY_EXIST
            return 'IS_FILE_EXIST' if info_dict == 'file' else 'IS_DIRECTORY_EXIST'

    def svn_get_filelist_under_directory(self, remote_path):
        """
        获取远端目录详细信息
        Author: Chenying
        :param remote_path: 目的路径
        :return: 深度，目的路径文件列表|IS_NOT_EXIST
        """

        remote_type = self.svn_info_is_file_or_directory(remote_path)

        if remote_type == 'IS_NOT_EXIST':
            return 'IS_NOT_EXIST'
        elif remote_type == 'IS_FILE_EXIST':
            return 'IS_FILE_EXIST'
        else:
            # SVN LIST命令
            svn_list_cmd = 'svn list ' + remote_path + ' --username ' + self._username + ' --password ' + \
                           self._password + ' --recursive'
        # 执行SVN INFO命令,逐行读取SVN INFO命令输出字符串
        run_cmd = OsUtil().popen_no_block(svn_list_cmd)
        # 返回一个包含各行字符串作为元素的列表
        list_splitlines_list = run_cmd.splitlines()

        directory_level_deep = max([list_line.count('/') for list_line in list_splitlines_list if not re.match(
            list_line, '/')])

        return directory_level_deep, list_splitlines_list

    def svn_export(self, remote_path, local_path):
        """
        检出
        Author: Chenying
        :param remote_path: 目的路径
        :param local_path: 本地路径
        :return: success，本地目录深度，本地路径目录文件列表|fail，本地路径目录文件确缺失列表
        """
        if not local_path[-1] == "/":
            local_path += "/"

        # SVN EXPORT命令
        svn_export_cmd = 'svn export ' + remote_path + ' ' + local_path + ' --username ' + self._username \
                         + ' --password ' + self._password + ' --force'

        # 执行SVN EXPORT命令
        OsUtil().popen_block(svn_export_cmd)

        # 验证本地文件列表是否匹配目的路径文件列表
        local_directories_and_files = []
        # 遍历输出本地目录及子目录，不包含隐藏目录
        [local_directories_and_files.append(
            os.path.join(rs, d[:]).replace(local_path, '').replace("\\", '/') + '/') for rs, ds, fs in
            os.walk(local_path) for d in ds if not d[0] == '.']
        # 遍历输出本地目录及子目录下所有的文件，不包含隐藏文件
        [local_directories_and_files.append(
            os.path.join(rs, f).replace(local_path, '').replace("\\", '/')) for rs, ds, fs in
            os.walk(local_path) for f in fs if not f[0] == '.']

        local_list = [local_info for local_info in local_directories_and_files]
        local_list.sort()
        local_deep_level = max(list_line.count('/') for list_line in local_list)

        remote_list = self.svn_get_filelist_under_directory(remote_path)[1]

        miss_list = [miss for miss in local_list if miss not in remote_list]

        return 'SUCCESS', local_deep_level, local_list if not miss_list else 'FAILED', miss_list

    def svn_mkdir(self, remote_path):
        """
        创建目的路径
        Author: Chenying
        :param remote_path: 目的路径
        :return: success：目的路径创建成功，远端路径信息|fail：目的路径创建失败

        """
        code = ['success', 'fail']

        # SVN MKDIR 命令
        svn_mkdir_cmd = 'svn mkdir ' + remote_path + ' -m "Create directory"' + ' --username ' + self._username + \
                        '--password ' + self._password

        # 判断远端路径是否存在
        if not self.svn_info(remote_path):
            OsUtil().popen_block(svn_mkdir_cmd)
        else:
            return '目的路径已存在！'

        # 验证目的路径是否创建
        remote_path_mkdir_dicts = self.svn_info(remote_path)

        if not remote_path_mkdir_dicts:
            return '目的路径创建失败！'
        else:
            return code[0], self.svn_info(remote_path)

    def svn_delete(self, remote_path):
        """
        删除目的路径
        Author: Chenying
        :param remote_path: 目的路径
        :return: success：目的路径删除成功|fail：目的路径删除失败，目的路径信息

        """
        code = ['success', 'fail']

        # SVN DELETE 命令
        svn_delete_cmd = 'svn delete -m "delete trunk" ' + remote_path + ' --username ' + self._username + \
                         ' --password ' + self._password

        # 判断远端路径是否存在
        if not self.svn_info(remote_path):
            return '目的路径不存在！'
        else:
            OsUtil().popen_block(svn_delete_cmd)

        # 验证目的路径是否删除
        remote_path_deleted_info = self.svn_info(remote_path)

        if not remote_path_deleted_info:
            return code[0]
        else:
            return code[1]

    def svn_add(self, remote_path, source_path):
        """
        上传文件
        Author: Chenying
        :param remote_path: 目的路径
        :param source_path: 源路径
        :return: success：目的路径文件上传成功|fail：目的路径文件上传失败，目的路径文件列表
        """
        code = ['success', 'fail']

        # SVN ADD 命令
        svn_add_cmd = 'svn --force add ' + source_path + ' --username ' + self._username + ' --password ' + \
                      self._password
        # SVN COMMIT 命令
        svn_commit_cmd = 'svn -m %Revision% commit ' + source_path + ' --username ' + self._username + \
                         ' --password ' + self._password

        OsUtil().popen_block(svn_add_cmd)
        OsUtil().popen_block(svn_commit_cmd)

        # 验证目的文件列表是否匹配源文件列表
        remote_list = self.svn_get_filelist_under_directory(remote_path)[1]

        source_list = self.svn_get_filelist_under_directory(source_path)[1]

        miss_list = [miss for miss in source_list if miss not in remote_list]

        if not miss_list:
            return code[0]
        else:
            return code[1], miss_list

    def svn_cp(self, remote_path, source_path):
        """
        复制文件
        Author: Chenying
        :param remote_path: 目的路径
        :param source_path: 源路径
        :return: success：目的路径文件上传成功|fail：目的路径文件上传失败，目的路径文件列表
        """
        code = ['success', 'fail']

        # SVN CP 命令
        svn_cp_cmd = 'svn -m "CP" cp ' + source_path + ' ' + remote_path + ' --username ' + self._username + \
                     ' --password ' + self._password

        OsUtil().popen_block(svn_cp_cmd)

        # 比较源路径的版本信息与目的路径最后一次修改的版本信息是否一致
        remote_info = self.svn_info(remote_path)
        source_info = self.svn_info(source_path)

        if not operator.eq(remote_info['Last Changed Rev'], source_info['Revision']):
            return code[1]
        else:
            return code[0]

    def svn_diff_text(self, path1, path2):
        """
        差异统计
        :param path1: 目录
        :param path2: 目录
        :return: subtractions_counts：sum_counts：差异总行数|删除的行数|additions_counts：新增的行数|difference_files: 差异文件总数
        """
        # SVN DIFF命令
        svn_diff_cmd = 'svn diff ' + path1 + ' ' + path2 + ' --username ' + self._username + \
                       ' --password ' + self._password

        # 执行SVN DIFF命令并输出到屏幕
        result = OsUtil().popen_block2(svn_diff_cmd)
        if result.get("status"):
            diff_splitlines_list = result.get("message").decode('utf-8','ignore').strip().splitlines()
        else:
            return {
                "status": "error",
                "message": result.get("message").decode('utf-8')
            }


        # 列出所有差异列表
        special_chars_lists1 = [special_chars for special_chars in diff_splitlines_list if special_chars != ''
                                # 去除所有特殊字符行
                                if not special_chars.startswith('Index: ')
                                if not special_chars.startswith('===')
                                if not special_chars.startswith('--- ')
                                if not special_chars.startswith('+++ ')
                                if not special_chars.startswith('@@ ')
                                if not special_chars.startswith('Cannot display: ')
                                if not special_chars.startswith('svn:')
                                if not special_chars.startswith('Property changes on: ')
                                if not special_chars.startswith('Deleted: ')
                                if not special_chars.startswith('##')
                                if not special_chars.startswith('-application/')
                                if not special_chars.startswith('+application/')
                                if not special_chars.startswith('\\')
                                if not special_chars.startswith('___')
                                if not special_chars.startswith('Added:')
                                if not special_chars.startswith(' ')
                                if not special_chars.startswith('Modified:')]

        special_chars_lists2 = list(set(special_chars for special_chars in diff_splitlines_list if special_chars !=
                                        '' if special_chars.startswith('Index: ')))

        special_chars_lists = special_chars_lists1 + special_chars_lists2
        print(special_chars_lists2)

        # 统计新增、删除次数以及差异文件数量，以字典返回{'+': , '-': 'I': }
        additions_subtractions_counts_dict = Counter(
            [additions_subtractions_lists[:1] for additions_subtractions_lists in special_chars_lists])

        additions_counts = additions_subtractions_counts_dict['+']
        subtractions_counts = additions_subtractions_counts_dict['-']
        sum_counts = additions_counts + subtractions_counts

        difference_files = additions_subtractions_counts_dict['I']
        return {
            "status":"success",
            "message":{
            'total': "{0}".format(sum_counts),
            'add_count': "{0}".format(additions_counts),
            'del_count': "{0}".format(subtractions_counts),
            'difference_files': "{0}".format(difference_files)
        }}


    def svn_get_filenums_under_directory(self, remote_path):
        """
        获取路径下的文件总数
        :param remote_path: 远端路径
        :return: 文件总数
        """
        under_directories_list = self.svn_get_filelist_under_directory(remote_path)[1]
        files_under_directories_numbers = len([files for files in under_directories_list if not files[-1] == '/'])

        return files_under_directories_numbers
