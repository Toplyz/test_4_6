# -*- coding: utf-8 -*-
# Time : 2024/2/24 17:34
# Author : lyz
# File : test_page1.py
# Desc :
import unittest
from time import sleep

from objectpage.login_page import LoginPage

from config.config import url, driver_path, system_version
from log.log import loggers


class TestCases:
    def test_1(self, login):
        '''
        验证有效的用户名和密码成功登录系统
        :return:
        '''
        print('登陆的第一个测试用例')
        self.driver = login
        self.loginpage = LoginPage(self.driver)
        # 登录禅道
        self.loginpage.input_username('admin')
        self.loginpage.input_password('lyz1108..')
        self.loginpage.click_login()
        sleep(0.5)
        # 加入断言
        assert '我的地盘 - 禅道' in self.driver.title
        self.loginpage.click_logout()
        loggers.info('有效的用户名和密码成功登录系统')

    # @unittest.skip('不执行该测试用例')
    @unittest.skipIf(system_version == '1.1', reason='只有版本号为1.2的时候执行')
    def test_2(self):
        '''
        验证密码为空时登录失败
        :return:
        '''
        print('登录的第二个测试用例')
        self.loginpage.input_username('admin')
        self.loginpage.click_login()
        sleep(0.5)
        alert_login = self.driver.switch_to.alert
        alert_login.accept()
