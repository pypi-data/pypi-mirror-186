# -*- coding:UTF-8 -*-
import xml.etree.ElementTree as et
import xml.dom.minidom as mn
# import numpy as np
# import pandas as pd
from collections import defaultdict
from functools import reduce


class XmlUtil(object):
    def __init__(self, xml_file):
        self._xml_file = xml_file

    def analysis_key_get_value(self, root_tag, tag_key):
        """
        返回目标key下的value
        :param root_tag: 目标
        :param tag_key: key
        :return: 
        """
        # 读取XML文件
        tree = et.parse(self._xml_file)
        # 判断ROOT_TAG是否存在
        if tree.find(root_tag) is None:
            return root_tag + ' IS NOT EXIST'
        else:
            root = tree.find(root_tag)

        # 判断TAG_KEY是否存在
        if root.find(tag_key) is None:
            return tag_key + ' IS NOT EXIST'

        values = ['NONE' if value is None else 'ERROR' if not len(value.split(',')) == 1 else value for value in
                  [key.text for key in root.iter(tag_key)]]

        return ', '.join(values)

    def analysis_key_get_dict(self, root_tag):
        """
        输入单层的key ，返回一个字典
        :param root_tag: tag
        :return: dict
        """
        # 读取XML文件
        tree = et.parse(self._xml_file)

        # 判断ROOT_TAG是否存在
        if tree.find(root_tag) is None:
            return root_tag + ' IS NOT EXIST'
        else:
            tag = tree.find(root_tag)

        key_value_lists = ['NONE' if value is None else ''.join(value).split(',') for value in
                           [child.tag + ',' + ('NONE' if child.text is None else child.text) for child in tag]]

        merge_dict = dict(reduce(lambda x, d: x[d[0]].append(d[1]) or x, key_value_lists, defaultdict(list)))

        keys = [key for key in merge_dict.keys()]
        values = [''.join(value) if len(value) == 1 else value for value in merge_dict.values()]

        dicts = dict(zip(keys, values))

        return dicts

    def analysis_key_get_values(self, root_tag):
        """
        xml库读取4层结构
        :param root_tag: tag
        :return: dict
        """
        # 读取XML文件
        tree = et.parse(self._xml_file)

        # 判断ROOT_TAG是否存在
        if tree.find(root_tag) is None:
            return root_tag + ' IS NOT EXIST'
        else:
            tag = tree.find(root_tag)

        key_value_lists = ['NONE' if value is None else ''.join(value).split(',') for value in
                           [child.tag + ',' + ('NONE' if child.text is None else child.text) for child in tag]]

        merge_dict = dict(reduce(lambda x, d: x[d[0]].append(d[1]) or x, key_value_lists, defaultdict(list)))

        keys = [key for key in merge_dict.keys()]
        values = [''.join(value) if len(value) == 1 else value for value in merge_dict.values()]

        dicts = dict(zip(keys, values))

        for key, value in dicts.items():
            if "\n" in value:
                d_key = key
                rank = tree.findall(root_tag)[0].find(d_key)
                t_keys = []
                t_values = []
                for i in rank:
                    t_keys.append(i.tag)
                    t_values.append(i.text)
                t_dict = dict(zip(t_keys, t_values))
                dicts[d_key] = t_dict

        return dicts

    # def pandas_xml(self, root_tag):
    #     tree = et.parse(self._xml_file)
    #     root = tree.find(root_tag)
    #
    #     list1 = []
    #     list2 = []
    #
    #     nodes = root.findall(".//")
    #
    #     for node in nodes:
    #         if node.text is None:
    #             list1.append(node.tag + "," + "None")
    #         else:
    #             list2.append(node.tag + ", " + node.text)
    #
    #     for i in list2:
    #         str_list2=str(i).split(",")
    #         print(str_list2)
    #         if "\n" in str_list2[-1]:
    #             print(i)