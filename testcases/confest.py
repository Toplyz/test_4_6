# -*- coding: utf-8 -*-
# Time : 2024/2/26 13:52
# Author : lyz
# File : confest.py
# Desc :
import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from config.config import url,driver_path

@pytest.fixture(scope='session')
def login():
    # 找到驱动路径，然后找到浏览器驱动
    e = Service(executable_path=driver_path)
    driver = webdriver.Edge(service=e)
    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit()