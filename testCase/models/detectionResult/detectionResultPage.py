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

class DetectionResultPage(BasePage):

    # 定位检测结果
    detectionResult_button_loc=(By.XPATH,".//*[@id='accountInfo']/a")
    # 定位页面title：论文检测详细信息
    pageTitle_loc=(By.XPATH,"html/body/div[4]/div[2]/p")

    # 检测条件-相似比-左边界
    query_ratioBegin_loc=(By.XPATH,".//*[@id='searchTaskItemForm']/div/p/span[1]/input")
    # 检测条件-相似比-右边界
    query_ratioEnd_loc=(By.XPATH,".//*[@id='searchTaskItemForm']/div/p/span[3]/input")
    # 检测条件-篇名 输入框
    query_fileTitle_loc=(By.XPATH,".//*[@id='searchTaskItemForm']/div/p/input[1]")
    # 检测条件-作者 输入框
    query_author_loc=(By.XPATH,".//*[@id='authorInput']")
    # 检测条件-检测时间-左边界
    query_begintimeImg_loc=(By.XPATH,"")
    # 检测条件-检测时间-右边界
    query_endtimeImg_loc=(By.XPATH,"")
    # 检测条件-任务名称-下拉框
    query_taskTitle_loc=(By.XPATH,".//*[@id='taskNameSelectArrow']")
    # 检测条件-问题论文-勾选框
    #query_isTroubleFile_loc=(By.XPATH,".//*[@id='isTrouble']")
    query_isTroubleFile_loc=(By.ID,"isTrouble")
    # 定位 查询按钮
    query_button_loc=(By.XPATH,".//*[@id='searchTaskItemForm']/div/input[2]")


    # 没有检索到符合检索条件的记录，提示：没有找到您要搜索的任务。
    query_isNull_loc=(By.XPATH,"html/body/div[4]/div[2]/p[2]")
    # 定位 检测结果列表-第一条记录的篇名
    resultList_fileTitle1_loc=(By.XPATH,"html/body/div[4]/div[2]/table/tbody/tr[2]/td[4]/a")
    # 定位 检测结果列表-第一条记录的作者
    resultList_author_loc=(By.XPATH,"html/body/div[4]/div[2]/table/tbody/tr[2]/td[5]/a")


    # 定位 记录总条数
    pageSum_loc=(By.XPATH,"html/body/div[4]/div[2]/form[2]/p/span[1]/b")


    def pageSum(self):
        '''返回记录总条数'''
        pagesum=self.find_element(*self.pageSum_loc).text
        return pagesum

    def queryIsNull(self):
        '''没有检索到复合检索条件的记录，返回提示信息“没有找到您要搜索的任务。”'''
        message=self.find_element(*self.query_isNull_loc).text
        return message




    def inDetectResult(self):
        '''点击检测结果按钮，进入检测结果页面'''
        self.find_element(*self.detectionResult_button_loc).click()

    def pageTitle(self):
        '''返回页面title：论文检测详细信息'''
        title=self.find_element(*self.pageTitle_loc).text
        return title

    def queryButtonClick(self):
        '''点击查询按钮'''
        self.find_element(*self.query_button_loc).click()
        sleep(10)

    def inputRatioBegin(self,retiobegin):
        '''输入相似比-左边界值'''
        self.find_element(*self.query_ratioBegin_loc).clear()
        self.find_element(*self.query_ratioBegin_loc).send_keys(retiobegin)

    def inputRatioEnd(self,retioend):
        '''输入相似比-右边界值'''
        self.find_element(*self.query_ratioEnd_loc).clear()
        self.find_element(*self.query_ratioEnd_loc).send_keys(retioend)

    def inputFileTitle(self,filetitle):
        '''输入篇名'''
        self.find_element(*self.query_fileTitle_loc).clear()
        self.find_element(*self.query_fileTitle_loc).send_keys(filetitle)

    def inputAuthor(self,author):
        '''输入作者'''
        self.find_element(*self.query_author_loc).clear()
        self.find_element(*self.query_author_loc).send_keys(author)

    def resultListFileTitle1(self):
        '''返回检测结果列表-第一条记录的篇名'''
        title=self.find_element(*self.resultList_fileTitle1_loc).text
        return title

    def resultListAuthor(self):
        '''返回检测结果列表-第一条记录的篇名'''
        author=self.find_element(*self.resultList_author_loc).text
        return author


