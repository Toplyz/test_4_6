# -*- coding: utf-8 -*-
# Time : 2024/2/26 14:04
# Author : lyz
# File : run_pytest.py.py
# Desc :
import pytest
import subprocess

pytest.main()
subprocess.call('allure generate ./result/temp -o ./result/report --clean',shell=True)
subprocess.call('allure open -h 127.0.0.1 -p 8883 ./result/report',shell=True)

