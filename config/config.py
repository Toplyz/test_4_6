# -*- coding: utf-8 -*-
# Time : 2024/2/24 21:17
# Author : lyz
# File : config.py
# Desc :
import os

root_path = os.path.dirname(os.path.dirname(__file__))

url = 'http://127.0.0.1/zentao/user-login.html'
driver_path = root_path + r'\driver\msedgedriver.exe'
case_path = root_path + r'\test_demo'
report_path = root_path + r'\report'
log_file = root_path + r'/log/log.txt'
# 版本号
system_version = '1.1'
