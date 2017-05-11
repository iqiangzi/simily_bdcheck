#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-04-28 10:01:52
# @Author  : Nxy
# @Site    :
# @File    : informationManagement.py
# @Software: PyCharm
from selenium import  webdriver
import unittest
from testCase.pageObj.basePage import BasePage
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os
from util.toolUtils.getPath import GetPath
from selenium.webdriver.common.keys import Keys
from time import sleep

class InformationManagement(BasePage):

    # 定位管理中心
    manageCenter_button_loc=(By.ID,"manageCenter")
    # 定位管理中心 -- 信息管理
    information_button_loc=(By.XPATH,".//*[@id='manageCenterList']/li[2]/a")

    # 查询按钮
    query_button_loc=(By.XPATH,".//*[@id='searchTaskForm']/div/input")
    # 检索条件 -- 账户 -- 下拉选择框
    query_account_loc=(By.XPATH,".//*[@id='userIdSelect']")
    # 检索条件 -- 任务名称 -- 输入框
    query_taskname_loc=(By.ID,"taskNameInput")
    # 检索条件 -- 创建时间（开始） -- 输入框
    query_begintime_loc=(By.ID,"beginDateInput")
    # 检索条件 -- 创建时间（结束） -- 输入框
    query_endtime_loc=(By.ID,"endDateInput")

    # 没有检索到符合检索条件的记录，提示：没有找到您要搜索的任务。
    query_isNull_loc=(By.XPATH,"html/body/div[4]/div[2]/p")
    # 输入检索条件后，检索结果列表第一条记录的任务名
    query_firstName_loc=(By.XPATH,"html/body/div[4]/div[2]/table/tbody/tr[2]/td[3]/a")

    # 定位每页显示按钮
    paging_button_lco=(By.ID,"sel")
    # 每页显示10
    paging_button10_lco=(By.ID,"10")
    # 每页显示20
    paging_button20_lco=(By.ID,"20")
    # 每页显示50
    paging_button50_lco=(By.ID,"50")
    # 定位记录总条数
    #collegePage_sum_loc=(By.XPATH,"html/body/div[4]/div[2]/form[2]/p/span[1]/b")

    collegePage_sum_loc=(By.XPATH,"html/body/div[4]/div[2]/p")




    def inInfoManage(self):
        # 进入管理中心--信息管理
        # 该方法不可用，悬浮不行，直接输入url进入
        '''鼠标悬停在管理中心，然后点击信息管理'''
        above=self.find_element(*self.manageCenter_button_loc)
        ActionChains(self.driver).move_to_element(above).perform()
        # 悬浮后，点击信息管理
        sleep(5)
        self.find_element(*self.information_button_loc).click()

    def queryButtonClick(self):
        '''点击查询按钮'''
        self.find_element(*self.query_button_loc).click()

    def inputTaskName(self,taskName):
        '''输入任务名称检索条件，进行检索'''
        self.find_element(*self.query_taskname_loc).clear()
        self.find_element(*self.query_taskname_loc).send_keys(taskName)

    def queryFirstTaskName(self):
        '''输入检索条件后，返回检索结果列表第一条记录的任务名'''
        firstName=self.find_element(*self.query_firstName_loc).text
        return firstName

    def queryIsNull(self):
        '''没有检索到复合检索条件的记录，返回提示信息“没有找到您要搜索的任务。”'''
        message=self.find_element(*self.collegePage_sum_loc).text
        return message


    # 返回总的信息条数
    def pageMsg(self):
        return self.find_element(*self.collegePage_sum_loc).text


