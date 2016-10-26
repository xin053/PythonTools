#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
待完善：多线程requests

This file is used for running GPRS of my blog's pictures in 'https://i.imgur.com'
for not deleting these pictures.

please run this file at least one time every six months
"""

__title__ = 'GPRS_of_blog_pictures'
__version__ = '1.0'
__build__ = 0x1000
__author__ = 'xin053'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2016 xin053'

import os
import re
import requests

def main():
    dir_path = r"E:\Hexo\source\_posts"
    readme_path = r"E:\Hexo\README.md"
    hrefs = []

    # files in E:\Hexo\source\_posts
    for filename in os.listdir(dir_path):
        # print(filename)
        with open(dir_path + "\\" + filename, "r", encoding='utf8') as md_file:
            md_file_content = md_file.read()
            href = re.findall(r"https?\://i.imgur.com/\w+\.(?:jpg|jpeg|png|bmp|gif)", md_file_content)
            hrefs.extend(href)

    # README
    with open(readme_path, "r", encoding='utf8') as readme_file:
        read_file_content = readme_file.read()
        href = re.findall(r"https?\://i.imgur.com/\w+\.(?:jpg|jpeg|png|bmp|gif)", read_file_content)
        hrefs.extend(href)

    # print(hrefs)

    # run GPRS
    for href in hrefs:
        result = requests.get(href)
        # print(result.status_code)
        if result.status_code == 404:
            print(href + " is wrong!")

    print("OK!!!")


if __name__ == "__main__":
    main()
    exit()
