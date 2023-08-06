# -*- coding: utf-8 -*-
# @Author  : Smawe
# @Time    : 2023/1/18 16:12
# @File    : test.py
# @Software: PyCharm
import os
import re
from os.path import join
from lxml import etree

__all__ = ['sort', 'get_website_encode']


_mapping = {
    "零": 0, "一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9,
    "十": 10, "百": 100, "千": 1000, "万": 10000, "十万": 100000, "百万": 1000000,
    "两": 2
}

_need = {
    "十", "百", "千", "万", "十万", "百万"
}

_regexs = [r"\w*?第(.*?)章.*"]
_replace_regex = r".*\第(.*?)章.*"


def sort(src=""):
    """
    对目录中的文件进行重命名
    第某某章必须在10万章以下
    列如:
        第一百章.txt -> 第100章.txt
    :return:
    """
    if not src:
        raise ValueError("src cannot is empty")

    root_path = src

    for f in os.listdir(src):
        if not _isfile(f):
            continue

        if not re.match(_regexs[0], f):
            continue

        if re.match(_regexs[0], f).group(1).isdigit():
            continue

        old_path = join(root_path, f)
        map_text = _calculate(re.match(_regexs[0], f).group(1))
        new_path = old_path.replace(re.match(_regexs[0], f).group(1), str(map_text))
        os.rename(src=old_path, dst=new_path)


def _isfile(f: str):
    if f.__contains__(".") and f.rsplit(".", maxsplit=1)[-1]:
        return True

    return False


def _calculate(s: str):
    # 十一, 一千零一,三千九百五十
    temp_result = 0
    temp_num = 1
    result = 0

    s = s.strip()

    if len(s) == 1:
        return _mapping[s]

    if len(s) == 2:
        if s[0] not in _need:
            return _mapping[s[0]] * _mapping[s[1]]

        return _mapping[s[0]] + _mapping[s[1]]

    for i, v in enumerate(s):
        if i != len(s) - 1:
            if s[i] not in _need and s[i + 1] in _need:
                # temp_result = mapping[temp] * mapping[s[i]]
                temp_num = _mapping[s[i]]

        if s[i] in _need:
            result += temp_num * _mapping[s[i]]
            result += temp_result
            continue

        if i <= len(s) - 3:
            if s[i] not in _need and s[i + 1] not in _need and s[i + 2] in _need:
                temp_result = _mapping[s[i]]
        else:
            if len(s[i:]) == 2:
                if s[i] not in _need and s[i+1] in _need:
                    result += _mapping[s[i]] * _mapping[s[i + 1]]
                    return result
                result += _mapping[s[i]] + _mapping[s[i + 1]]
                return result
            result += _mapping[s[i]]
            return result


def get_website_encode(html):
    """If no match is found, utf-8 is returned by default"""
    html_ = etree.HTML(html)
    r = html_.xpath(".//meta")
    for e in r:
        for i in e.values():
            match = re.search(r'charset=(.*)\s*', i, re.S)
            if match:
                return match.group(1)
    return 'utf-8'


if __name__ == '__main__':
    sort(r"D:\Test\example\千千小说万古神帝")
    # print(_calculate("一百"))
