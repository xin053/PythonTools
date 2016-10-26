#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
待完善：多线程update

update all python packages through pip
"""

__title__ = 'update_all_py_packages'
__version__ = '1.0'
__build__ = 0x1000
__author__ = 'xin053'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2016 xin053'

import subprocess
import re

def main():
    output = subprocess.getoutput('pip list --outdated')
    if output == '':
        print("all packages are up to date")
        return
    package_list = output.split('\n')

    for package in package_list:
        package_name = re.findall(r"\w+", package)[0]

        flag = True
        while flag:
            p=subprocess.Popen("pip install -U " + package_name, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            stdoutput,erroutput = p.communicate()
            flag = False
            if erroutput != '':
                flag = True

        print(package_name + " update successfully")

    print("Done")
    output = subprocess.getoutput('pip list --outdated')
    if output == '':
        print("all packages are up to date")
    else:
        print("something is wrong")

if __name__ == "__main__":
    main()
    exit()
