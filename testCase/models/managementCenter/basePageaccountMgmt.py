#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/13 13:25
# @Author  : Nxy
# @Site    :
# @File    : BasePage.py
# @Software: PyCharm
from testCase.models import myUnitFirefox
from selenium import webdriver
import unittest
from time import sleep
from selenium.webdriver.common.by import By
class BasePage(object):
    '''
    页面基础类，用于账户信息页面的继承

    '''
    #账户信息URL
    burl="http://check.test.wanfangdata.com.cn/bd/Manage/Account"

    def __init__(self,selenium_driver,base_url= burl,parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent

    def _open(self,url):
        url = self.base_url +url
        self.driver.get(url)


    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)

    def open(self,url):
        self._open(url)

    def script(self,src):
        return self.driver.execute_script(src)
    #处理弹出窗口，注意是确认窗口
    def confirm_window(self):
        return self.driver.switch_to.alert().text
    #frame转换
    def user_login_switch(self,id):
        self.driver.switch_to.frame(id)
    #跳到最外层窗口
    def user_switch_default(self):
        self.driver.switch_to.default_content()

class UserVer(BasePage):
    #登录各个元素定位
    login_username_loc=(By.ID,"userid")
    login_password_loc=(By.ID,"password")
    login_button_loc=(By.XPATH,"/html/body/form/div[5]/div/div[1]/div[6]/input")

    def userLogin(self,username,password):
        '''
        用户登录
        :param username: 用户名
        :param password: 用户登录密码
        :return: 无返回值
        '''
        '''获取的用户名密码登录'''
        self.open("")
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(5)

    #登录用户名
    def login_username(self,username):
        self.find_element(*self.login_username_loc).clear()
        self.find_element(*self.login_username_loc).send_keys(username)
    #登录密码
    def login_password(self,password):
        self.find_element(*self.login_password_loc).clear()
        self.find_element(*self.login_password_loc).send_keys(password)
    #登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

if __name__=='__main__':
   unittest.main()