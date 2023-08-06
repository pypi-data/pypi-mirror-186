# -*- coding:UTF-8 -*-
import logging

from atlassian import Confluence, utils

import jieba.posseg as pseg


class ConfluenceUtil(object):
    """
    Confluence Util
    Author: chenying
    """

    def __init__(self, url, username, password):
        # 初始化atlassian-python-api库的confluence model实例
        self.confluence = Confluence(
            url=url,
            username=username,
            password=password
        )

        logging.basicConfig(level=logging.CRITICAL)

    def _get_space_key_by_space_name(self, space_name):
        """
        Get space key for space name
        Author: chenying
        :param space_name: SPACE NAME
        :return: Space Key
        """
        # 获取所有空间信息列表
        spaces_list = self.confluence.get_all_spaces()

        try:
            # 根据空间显示名筛选空间名对应的SPACE KEY
            space_key = spaces_list[next(index for (index, d) in enumerate(spaces_list) if d['name'] == space_name)][
                'key']

            return space_key
        except Exception as ex:
            print(ex)
            return 'FAIL', "Can't find {space_name} page in the {url}".format(space_name=space_name,
                                                                              url=self.confluence.url)

    def _get_page_version(self, space_name, title):
        space = self._get_space_key_by_space_name(space_name)
        page_id = self.confluence.get_page_id(space, title)
        page_body_value = self.confluence.get_page_by_id(page_id).get("version").get("number")

        return page_body_value

    @staticmethod
    def _create_list(data):
        """
        Create confluence page list power
        Author: chenying
        :param data: datas
        :return:
        """
        value = "<p>"

        for item in data:
            value += "{}<br />".format(item)

        return value + "</p>"

    @staticmethod
    def _create_jira_filet_no_column():
        """
        Create JIRA Filter no column
        Author: chenying
        :return: XHTML
        """
        value = """<p>
            <ac:structured-macro ac:name="jira">
               <ac:parameter ac:name="server">JIRA</ac:parameter>
               <ac:parameter ac:name="serverId">e78bf60f-8e47-4183-9f26-9e9661fc2ce8</ac:parameter>
               <ac:parameter ac:name="key">{}</ac:parameter>
               </ac:structured-macro>
        </p>"""
        return value

    @staticmethod
    def _create_jira_filet_jql_no_columns():
        """
        Create JIRA Filter JQL no column
        Author: chenying
        :return: XHTML
        """
        value = """<p>
            <ac:structured-macro ac:name="jira">
               <ac:parameter ac:name="server">JIRA</ac:parameter>
               <ac:parameter ac:name="serverId">e78bf60f-8e47-4183-9f26-9e9661fc2ce8</ac:parameter>
               <ac:parameter ac:name="jqlQuery">{}</ac:parameter>
            </ac:structured-macro>
        </p>"""
        return value

    @staticmethod
    def _jql_is_name(data):
        """
        Judgment JQLQuery is a name
        Author: chenying
        :param data: JQLQuery
        :return: True:is name|False:isn`t a name
        """
        data_list = pseg.lcut(data)

        for eve_word, isxing in data_list:
            if isxing == "nr":
                return True

        return False

    @staticmethod
    def _create_jira_filet_jql_is_people_name():
        """
        Create JIRA Filter JQL no column
        Author: chenying
        :return: XHTML
        """
        value = """<p>
            <ac:structured-macro ac:name="jira">
               <ac:parameter ac:name="server">JIRA</ac:parameter>
               <ac:parameter ac:name="serverId">e78bf60f-8e47-4183-9f26-9e9661fc2ce8</ac:parameter>
               <ac:parameter ac:name="jqlQuery">assignee = {} OR reporter = {}</ac:parameter>
               </ac:structured-macro>
        </p>"""
        return value

    @staticmethod
    def _create_jira_filet_jql_is_people_name_has_columns():
        """
        Create JIRA Filter JQL has column
        Author: chenying
        :return: XHTML
        """
        value = """<p>
                <ac:structured-macro ac:name="jira">
                   <ac:parameter ac:name="server">JIRA</ac:parameter>
                   <ac:parameter ac:name="serverId">e78bf60f-8e47-4183-9f26-9e9661fc2ce8</ac:parameter>
                   <ac:parameter ac:name="jqlQuery">assignee = {} OR reporter = {}</ac:parameter>
                   <ac:parameter ac:name="columns">{}</ac:parameter>
                   </ac:structured-macro>
            </p>"""
        return value

    @staticmethod
    def _create_jira_filet_jql_is_str_no_columns():
        """
        Create JIRA Filter JQL no column
        Author: chenying
        :return: XHTML
        """
        value = """<p>
                <ac:structured-macro ac:name="jira">
                   <ac:parameter ac:name="server">JIRA</ac:parameter>
                   <ac:parameter ac:name="serverId">e78bf60f-8e47-4183-9f26-9e9661fc2ce8</ac:parameter>
                   <ac:parameter ac:name="jqlQuery">summary ~ {} OR description ~ {}</ac:parameter>
                   </ac:structured-macro>
            </p>"""
        return value

    @staticmethod
    def _create_jira_filet_jql_is_str_has_columns():
        """
        Create JIRA Filter JQL has column
        Author: chenying
        :return: XHTML
        """
        value = """<p>
                    <ac:structured-macro ac:name="jira">
                       <ac:parameter ac:name="server">JIRA</ac:parameter>
                       <ac:parameter ac:name="serverId">e78bf60f-8e47-4183-9f26-9e9661fc2ce8</ac:parameter>
                       <ac:parameter ac:name="jqlQuery">summary ~ {} OR description ~ {}</ac:parameter>
                       <ac:parameter ac:name="columns">{}</ac:parameter>
                       </ac:structured-macro>
                </p>"""
        return value

    @staticmethod
    def _create_jira_filet_jql_has_columns():
        """
        Create JIRA Filter JQL with column
        Author: chenying
        :return: XHTML
        """
        value = """<p>
                <ac:structured-macro ac:name="jira">
                   <ac:parameter ac:name="server">JIRA</ac:parameter>
                   <ac:parameter ac:name="serverId">e78bf60f-8e47-4183-9f26-9e9661fc2ce8</ac:parameter>
                   <ac:parameter ac:name="jqlQuery">{}</ac:parameter>
                   <ac:parameter ac:name="columns">{}</ac:parameter>
                   </ac:structured-macro>
            </p>"""
        return value

    @staticmethod
    def _create_table(ordering, datas):
        """
        Create table by ordering and datas
        Author: chenying
        :param ordering: table headers
        :param datas: table data
        :return: table
        """
        data = []

        for value in datas:
            dict_list = (dict(zip(ordering, value)))
            data.append(dict_list)

        result = utils.html_table_from_dict(data, ordering)

        return result

    @staticmethod
    def _get_page_id_by_url(url):
        """
        Get Page ID
        Author: chenying
        :param url: URL
        :return: page_id
        """
        return ''.join(url).split('=')[-1]

    def create_confluence_page(self, space_name, parent_title, title, body):
        """
        1.Update page body if it is exists.
        2.Create a page if it is not exists
        Author: chenying
        :param space_name: SPACE NAME
        :param parent_title: parent page title
        :param title: title
        :param body: body
        :return: SUCCESS,URL|FAIL,MESSAGE
        """
        space_key = self._get_space_key_by_space_name(space_name)

        if "FAIL" in space_key:
            return space_key

        if self.confluence.get_page_by_title(space_key, parent_title) is None:
            return 'FAIL', "Can't find '{parent_title}' page in the '{space_name}'".format(parent_title=parent_title,
                                                                                           space_name=space_name)

        parent_id = self.confluence.get_page_id(space_key, title=parent_title)
        update_or_create_page_dict_info = self.confluence.update_or_create(parent_id, title, body,
                                                                           representation="wiki")

        return 'SUCCESS', '{host}{url}'.format(host=self.confluence.url,
                                               url=((update_or_create_page_dict_info or {}).get('_links') or {}).get(
                                                   'webui'))

    def clean_confluence_page(self, space_name, title):
        """
        Clean page body if already exist
        Author: chenying
        :param space_name: SPACE NAME
        :param title: title
        :return: SUCCESS,URL|FAIL,MESSAGE
        """
        space_key = self._get_space_key_by_space_name(space_name)

        if "FAIL" in space_key:
            return space_key

        if self.confluence.page_exists(space_key, title) is True:
            clean_page_dict_info = self.confluence.update_existing_page(self.confluence.get_page_id(space_key, title),
                                                                        title, body="")

            return 'SUCCESS', '{host}{url}'.format(host=self.confluence.url,
                                                   url=((clean_page_dict_info or {}).get('_links') or {}).get(
                                                       'webui'))
        else:
            return 'FAIL', "Can't find '{title}' page in the '{space_name}'".format(title=title, space_name=space_name)

    def append_confluence_list(self, space_name, title, data):
        """
        Append confluence page list
        Author: chenying
        :param space_name: SPACE NAME
        :param title: title
        :param data: list data
        :return: SUCCESS,URL|FAIL,MESSAGE
        """
        data_list = []

        for value in data:
            data_list.append("".join(value).replace(",", ", "))

        space_key = self._get_space_key_by_space_name(space_name)

        if "FAIL" in space_key:
            return space_key

        # 判断confluence页面是否存在
        if self.confluence.page_exists(space_key, title) is True:
            page_id = self.confluence.get_page_id(space_key, title)

            # 追加列表
            append_page_dict_info = self.confluence.append_page(page_id, title, self._create_list(data_list))

            return 'SUCCESS', '{host}{url}'.format(host=self.confluence.url,
                                                   url=((append_page_dict_info or {}).get('_links') or {}).get('webui'))
        else:
            return 'FAIL', "Can't find '{title}' page in the '{space_name}'".format(title=title, space_name=space_name)

    def append_confluence_dict(self, space_name, title, data):
        """
        Transfer dict to list append into confluence page
        Author: chenying
        :param space_name: SPACE NAME
        :param title: title
        :param data: dict data
        :return: SUCCESS,URL|FAIL,MESSAGE
        """
        dicts = []
        str_list = []

        for lists in data:
            dicts_list = []

            for key, value in lists.items():
                dicts_list.append(key + "=" + value)
            dicts.append(dicts_list)

        for value in dicts:
            str_list.append(", ".join(value))

        space_key = self._get_space_key_by_space_name(space_name)

        if "FAIL" in space_key:
            return space_key

        # 判断confluence页面是否存在
        if self.confluence.page_exists(space_key, title) is True:
            page_id = self.confluence.get_page_id(space_key, title)

            append_page_dict_info = self.confluence.append_page(page_id, title, self._create_list(str_list))

            return 'SUCCESS', '{host}{url}'.format(host=self.confluence.url,
                                                   url=((append_page_dict_info or {}).get('_links') or {}).get(
                                                       'webui'))
        else:
            return 'FAIL', "Can't find '{title}' page in the '{space_name}'".format(title=title, space_name=space_name)

    def append_confluence_table(self, space_name, title, ordering, data):
        """
        Append confluence page table
        Author: chenying
        :param space_name: SPACE NAME
        :param title: title
        :param ordering: table headers
        :param data: table data
        :return: SUCCESS,URL|FAIL,MESSAGE
        """
        space_key = self._get_space_key_by_space_name(space_name)

        if "FAIL" in space_key:
            return space_key

        # 判断confluence页面是否存在
        if self.confluence.page_exists(space_key, title) is True:
            page_id = self.confluence.get_page_id(space_key, title)

            # 追加表格
            append_page_dict_info = self.confluence.append_page(page_id, title, self._create_table(ordering, data))

            return 'SUCCESS', '{host}{url}'.format(host=self.confluence.url,
                                                   url=((append_page_dict_info or {}).get('_links') or {}).get(
                                                       'webui'))
        else:
            return 'FAIL', "Can't find '{title}' page in the '{space_name}'".format(title=title, space_name=space_name)

    def append_confluence_image(self, space_name, title, image_file):
        """
        Append confluence page image
        Author: chenying
        :param space_name: SPACE NAME
        :param title: title
        :param image_file: image file
        :return: SUCCESS,URL|FAIL,MESSAGE
        """
        space_key = self._get_space_key_by_space_name(space_name)

        if "FAIL" in space_key:
            return space_key

        # 判断confluence页面是否存在
        if self.confluence.page_exists(space_key, title) is True:
            page_id = self.confluence.get_page_id(space_key, title)

            # 将图片作为附件上传到confluence页面
            attach_file_dict_info = self.confluence.attach_file(image_file, page_id)
            attach_file_url = '{host}{url}'.format(host=self.confluence.url,
                                                   url=((attach_file_dict_info or {}).get('_links') or {}).get(
                                                       'thumbnail'))
            value = """<p>
                <ac:image>
                    <ri:url ri:value="{}"/>
                </ac:image>
            </p>""".format(attach_file_url)
            # 获取图片
            append_page_dict_info = self.confluence.append_page(page_id, title, value)

            return 'SUCCESS', '{host}{url}'.format(host=self.confluence.url,
                                                   url=((append_page_dict_info or {}).get('_links') or {}).get(
                                                       'webui'))
        else:
            return 'FAIL', "Can't find '{title}' page in the '{space_name}'".format(title=title, space_name=space_name)

    def append_confluence_jira_filter(self, space_name, title, body, columns=None):
        """
        Append JIRA Filter
        Author: chenying
        :param space_name: SPACE NAME
        :param title: title
        :param body: Type:JQLQuery, People's name, JIRA_ID, JIRA_URL. JIRA_URL transfer to JIRA_ID
        :param columns: JIRA ISSUE Column's name
                        Note: Columns parameter doesn't work for JIRA_URL and JIRA_ID
        :return: SUCCESS,URL|FAIL,MESSAGE
        """
        keywords = ['key', 'summary', 'status', 'project', 'type', 'status', 'priority', 'resolution',
                    'affects version', 'fix version', 'component', 'labels', 'environment', 'description', 'links',
                    'assignee', 'reporter', 'due', 'created', 'updated', 'resolved', 'estimate', 'remaining',
                    'logged', 'development', 'agile', 'votes', 'watchers']

        space_key = self._get_space_key_by_space_name(space_name)

        if "FAIL" in space_key:
            return space_key

        # confluence页面存在
        if self.confluence.page_exists(space_key, title) is True:
            page_id = self.confluence.get_page_id(space_key, title)

            # 不指定显示列
            if columns is None:
                # 输入的是JIRA_URL
                if "".join(body).split(":")[0] == "http" and "".join(body).split("/")[-1].split("-")[0] == "JIRA":
                    jql_url_jira_id = "".join(body).split("/")[-1]

                    value = self._create_jira_filet_no_column().format(jql_url_jira_id)
                    append_page_dict_info = self.confluence.append_page(page_id, title, value)

                    return 'SUCCESS', '{host}{url}'.format(host=self.confluence.url, url=(
                            (append_page_dict_info or {}).get('_links') or {}).get('webui'))
                # 输入的是JIRA_ID
                if "".join(body).split(":")[0] != "http" and "".join(body).split("-")[0] == "JIRA":
                    jira_id = "".join(body)

                    value = self._create_jira_filet_no_column().format(jira_id)
                    append_page_dict_info = self.confluence.append_page(page_id, title, value)

                    return 'SUCCESS', '{host}{url}'.format(host=self.confluence.url, url=(
                            (append_page_dict_info or {}).get('_links') or {}).get('webui'))

                # 输入的是JQL查询语句
                for keyword in keywords:
                    if keyword in body.split("=")[0]:
                        value = self._create_jira_filet_jql_no_columns().format(body)
                        append_page_dict_info = self.confluence.append_page(page_id, title, value)

                        return 'SUCCESS', '{host}{url}'.format(host=self.confluence.url, url=(
                                (append_page_dict_info or {}).get('_links') or {}).get('webui'))

                # 输入的是人名
                if self._jql_is_name("".join(body)) is True:
                    value = self._create_jira_filet_jql_is_people_name().format(body, body)
                    append_page_dict_info = self.confluence.append_page(page_id, title, value)

                    return 'SUCCESS', '{host}{url}'.format(host=self.confluence.url, url=(
                            (append_page_dict_info or {}).get('_links') or {}).get('webui'))

                # 输入的是字符串
                value = self._create_jira_filet_jql_is_str_no_columns().format(body, body)
                append_page_dict_info = self.confluence.append_page(page_id, title, value)

                return 'SUCCESS', '{host}{url}'.format(host=self.confluence.url, url=(
                        (append_page_dict_info or {}).get('_links') or {}).get('webui'))
            # 指定显示列
            else:
                # 判断columns参数是否符合JIRA ISSUE列名规范
                for value in columns.split(','):
                    # 错误直接打断执行
                    if value not in keywords:
                        return 'Incorrect column parameter: {}'.format(
                            value), 'Please check the columns parameters, JIRA ISSUE allow use {}'.format(keywords)

                # 指定显示列参数对JIRA_URL不起作用
                if "".join(body).split(":")[0] == "http" and "".join(body).split("/")[-1].split("-")[0] == "JIRA":
                    return "FAIL", "Please remove the columns parameter."

                # 指定显示列参数对JIRA_ID不起作用
                if "".join(body).split(":")[0] != "http" and "".join(body).split("-")[0] == "JIRA":
                    return "FAIL", "Please remove the columns parameter."

                # 输入的是JQL查询语句
                for keyword in keywords:
                    if keyword in body.split("=")[0]:
                        value = self._create_jira_filet_jql_has_columns().format(body, columns)
                        append_page_dict_info = self.confluence.append_page(page_id, title, value)

                        return 'SUCCESS', '{host}{url}'.format(host=self.confluence.url, url=(
                                (append_page_dict_info or {}).get('_links') or {}).get('webui'))

                # 输入的是人名
                if self._jql_is_name("".join(body)) is True:
                    value = self._create_jira_filet_jql_is_people_name_has_columns().format(body, body, columns)
                    append_page_dict_info = self.confluence.append_page(page_id, title, value)

                    return 'SUCCESS', '{host}{url}'.format(host=self.confluence.url, url=(
                            (append_page_dict_info or {}).get('_links') or {}).get('webui'))
                # 输入的是字符串
                value = self._create_jira_filet_jql_is_str_has_columns().format(body, body, columns)
                append_page_dict_info = self.confluence.append_page(page_id, title, value)

                return 'SUCCESS', '{host}{url}'.format(host=self.confluence.url, url=(
                        (append_page_dict_info or {}).get('_links') or {}).get('webui'))
        # confluence页面不存在
        else:
            return 'FAIL', "Can't find '{title}' page in the '{space_name}'".format(title=title, space_name=space_name)

    def delete_confluence_page_by_title(self, space_name, title):
        """
        This method removes a page by the space key and the page title
        Author: chenying
        :param space_name: SPACE NAME
        :param title: title
        :return: SUCCESS|FAIL,MESSAGE
        """
        space_key = self._get_space_key_by_space_name(space_name)

        if "FAIL" in space_key:
            return space_key

        if self.confluence.page_exists(space_key, title) is True:
            page_id = self.confluence.get_page_by_title(space_key, title)['id']
            self.confluence.remove_page(page_id)

            return 'SUCCESS'
        else:
            return 'FAIL', "Can't find '{title}' page in the '{url}'".format(title=title, url=self.confluence.url)

    def get_confluence_page_url_by_title(self, space_name, title):
        """
        Return the first page on a piece of Content
        Author: chenying
        :param space_name: SPACE NAME
        :param title: title
        :return: SUCCESS,URL|FAIL,MESSAGE
        """
        space_key = self._get_space_key_by_space_name(space_name)

        if "FAIL" in space_key:
            return space_key

        if self.confluence.page_exists(space_key, title) is True:
            return 'SUCCESS', '{host}{url}'.format(host=self.confluence.url, url=(
                    (self.confluence.get_page_by_title(space_key, title) or {}).get("_links") or {}).get("webui"))
        else:
            return 'FAIL', "Can't find '{title}' page in the '{space_name}'".format(title=title,
                                                                                    space_name=space_name)

    def export_confluence_page_as_pdf(self, space_name, title, export_name):
        """
        Export page as standard pdf exporter
        Author: chenying
        :param space_name: Space name
        :param title: title
        :param export_name: export file name
        :return: SUCCESS|FAIL,MESSAGE
        """
        space_key = self._get_space_key_by_space_name(space_name)

        if "FAIL" in space_key:
            return space_key

        page_id = self.confluence.get_page_id(space_key, title)

        if page_id is not None:
            content = self.confluence.export_page(page_id)

            with open(export_name, "wb") as pdf:
                pdf.write(content)
                pdf.close()
                return "SUCCESS"
        else:
            return 'FAIL', "Can't find '{title}' page in the '{space_name}'".format(title=title,
                                                                                    space_name=space_name)

    def export_confluence_page_as_word(self, space_name, title, export_name):
        """
        Export page as standard word exporter
        Author: chenying
        :param space_name: Space name
        :param title: title
        :param export_name: export file name
        :return: SUCCESS|FAIL,MESSAGE
        """
        space_key = self._get_space_key_by_space_name(space_name)

        if "FAIL" in space_key:
            return space_key

        page_id = self.confluence.get_page_id(space_key, title)

        if page_id is not None:
            content = self.confluence.get_page_as_word(page_id)

            with open(export_name, "wb") as pdf:
                pdf.write(content)
                pdf.close()
                return "SUCCESS"
        else:
            return 'FAIL', "Can't find '{title}' page in the '{space_name}'".format(title=title,
                                                                                    space_name=space_name)

    def delete_confluence_page_by_url(self, url):
        """
        This method removes a page for the page id
        Author: chenying
        :param url: URL
        :return: SUCCESS|FAIL,MESSAGE
        """
        # Get page id
        page_id = self._get_page_id_by_url(url)

        try:
            self.confluence.remove_page(page_id)

            return 'SUCCESS'
        except Exception as ex:
            print(ex)
            return 'FAIL', 'Page: "{URL}", is not exists'.format(URL=url)

    def get_confluence_page_title_by_url(self, url):
        """
        Get page title by the URL
        Author: chenying
        :param url: URL
        :return: SUCCESS,title|FAIL,MESSAGE
        """
        page_id = self._get_page_id_by_url(url)

        try:
            get_page_by_id_dict_info = self.confluence.get_page_by_id(page_id)

            return 'SUCCESS', '{title}'.format(title=(get_page_by_id_dict_info or {}).get('title'))
        except Exception as ex:
            print(ex)
            return 'FAIL', 'Page: "{url}" is not exists'.format(url=url)

    def get_confluence_all_groups(self):
        """
        Get all confluence groups
        Author: chenying
        :return: list(group_name)
        """
        _groups = []

        for lists in self.confluence.get_all_groups():
            group_name = lists.get("name")
            _groups.append(group_name)

        return _groups

    def get_confluence_group_members(self, group_name):
        """
        Get confluence group members
        Author: chenying
        :param group_name: group_name
        :return: group members username, Type: [user_key, display_name, user_name]
        """
        _members = []

        if group_name not in self.get_confluence_all_groups():
            return "FAIL"

        for lists in self.confluence.get_group_members(group_name):
            users = lists.get("username")
            users_info = self.get_confluence_user_details_by_username(users)
            _members.append(users_info)

        return _members

    # def get_confluence_group_members_name(self, user_list):
    #     """
    #     Get group members info, member's info type: [user_key, display_name, user_name]
    #     Author: chenying
    #     :param user_list: group members
    #     :return: list([user_key, display_name, user_name])
    #     """
    #     user_info_list = []
    #     for user in user_list:
    #         user_name_list = self.get_confluence_user_details_by_username(user)
    #
    #         user_info_list.append(user_name_list)
    #
    #     return user_info_list

    def get_confluence_all_members(self):
        """
        Get all user info, info type: list([user_key, display_name, user_name])
        Author: chenying
        :return: list([user_key, display_name, user_name])
        """
        user_info = []
        groups = self.get_confluence_all_groups()

        for group in groups:
            for member in self.get_confluence_group_members(group):
                user_info.append(member)

        return user_info

    def get_confluence_user_details_by_username(self, username):
        """
        Get user displayName and username
        Author: chenying
        :param username: user_name
        :return: [user_key, display_name, user_name]|error_message
        """
        try:
            details_dict_info = self.confluence.get_user_details_by_username(username)

            user_username = details_dict_info.get("username")
            user_display_name = details_dict_info.get("displayName")
            user_user_key = details_dict_info.get("userKey")

            user_dict_info = [user_user_key, user_display_name, user_username]

            return user_dict_info
        except Exception as ex:
            error_message = str(ex)

            return error_message
