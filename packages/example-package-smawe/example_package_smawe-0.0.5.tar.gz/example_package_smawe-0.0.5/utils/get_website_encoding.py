# -*- coding: utf-8 -*-
# @Author  : Smawe
# @Time    : 2023/1/15 11:11
# @File    : get_website_encoding.py
# @Software: PyCharm

# -*- coding: utf-8 -*-
# @Author  : Smawe
# @Time    : 2022/10/13 21:38
# @File    : auto.py
# @Software: PyCharm
import re
from lxml import etree


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
    import requests
    # url = 'https://www.baidu.com'
    url = "https://www.qqtxt.cc/list/1_1.html"
    headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko)Chrome/105.0.0.0 Safari/537.36"
    }
    res = requests.get(url, headers=headers)
    print(get_website_encode(res.text))
