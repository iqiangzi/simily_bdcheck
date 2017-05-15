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
    # 检测条件-任务名称-下拉框内容-第一条（全部）
    query_taskTitle01_loc=(By.XPATH,".//*[@id='taskNameUl']/li[1]")
    # 检测条件-任务名称-下拉框内容-第二条（批量20170510105022）
    query_taskTitle02_loc=(By.XPATH,".//*[@id='taskNameUl']/li[2]")
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






    def clickIsTroubleFile(self):
        '''点击问题论文-勾选框，进行勾选和取消勾选操作'''
        self.find_element(*self.query_isTroubleFile_loc).click()

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

    def queryIsNull(self):
        '''没有检索到复合检索条件的记录，返回提示信息“没有找到您要搜索的任务。”'''
        message=self.find_element(*self.query_isNull_loc).text
        return message

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

    def taskNameSelectLi1(self):
        '''选择检索条件 -- 任务名称 -- 下拉选择框 第一个元素'''
        self.find_element(*self.query_taskTitle_loc).click()
        sleep(2)
        self.find_element(*self.query_taskTitle01_loc).click()

    def taskNameSelectLi2(self):
        '''选择检索条件 -- 任务名称 -- 下拉选择框 第二个元素'''
        self.find_element(*self.query_taskTitle_loc).click()
        sleep(2)
        self.find_element(*self.query_taskTitle02_loc).click()

    def pageSum(self):
        '''返回记录总条数'''
        pagesum=self.find_element(*self.pageSum_loc).text
        return pagesum

    def resultListFileTitle1(self):
        '''返回检测结果列表-第一条记录的篇名'''
        title=self.find_element(*self.resultList_fileTitle1_loc).text
        return title

    def resultListAuthor(self):
        '''返回检测结果列表-第一条记录的篇名'''
        author=self.find_element(*self.resultList_author_loc).text
        return author




    def queryBeginTime(self,year1,month1,day1):
        '''
        选择开始时间查询
        :param year1:开始日期中的年份，1998-2018
        :param month1:开始日期中的月份
        :param day1:开始日期中的日，注意，8，应该传入参数08，现在还不行
        :return:
        '''
        # 点击开始日期下拉框
        self.driver.find_element_by_css_selector("img.ui-datepicker-trigger").click()
        # 点击年份下拉框
        self.driver.find_element_by_css_selector(".ui-datepicker-year").click()
        # 选择年份
        self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div/div/select[1]/option[@value=%r]" % year1).click()
        sleep(2)
        # 点击月份下拉框
        self.driver.find_element_by_css_selector(".ui-datepicker-month").click()
        # 选择月份
        self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div/div/select[2]/option[%r]" % month1).click()
        sleep(2)
        # 选择日
        self.driver.find_element_by_link_text("%r" %day1).click()
        sleep(2)

    def queryEndTime(self,year2,month2,day2):
        '''
        选择结束时间查询
        :param year2:结束日期中的年份，1998-2018
        :param month2:结束日期中的月份
        :param day2:结束日期中的日
        :return:
        '''
        # 点击选择结束日期
        self.driver.find_element_by_xpath("(//img[@alt='...'])[2]").click()
        # 点击年份下拉框
        self.driver.find_element_by_css_selector(".ui-datepicker-year").click()
        # 选择年份
        self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div/div/select[1]/option[@value=%r]" % year2).click()
        sleep(2)
        # 点击月份下拉框
        self.driver.find_element_by_css_selector(".ui-datepicker-month").click()
        # 选择月份
        self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div/div/select[2]/option[%r]" % month2).click()
        sleep(2)
        # 选择日
        self.driver.find_element_by_link_text("%r" %day2).click()
        sleep(2)


    # 判断目录中是否存在同名文件 有的话返回True
    def downVerify1(self,newTitle):
        ab_path = GetPath().getAbsoluteFilePath(newTitle,r"downloadFiles\%s" % newTitle)
        flag = os.path.exists(ab_path)
        return flag

    # 判断文件夹是否为空，不为空则重命名同名文件，以保证新下载的文件的唯一性。为空则直接下载
    def renameFileName1(self,newTitle):
        ab_path = GetPath().getAbsoluteFilePath(newTitle,r"downloadFiles\%s" % newTitle)
        ab_path_rename = GetPath().getAbsoluteFilePath("%s" % newTitle,r"downloadFiles")
        #获取当前时间
        name=time.strftime("%Y-%m-%d %H_%M_%S")
        if os.path.exists(ab_path):
            os.rename(ab_path,ab_path_rename+"\%s.pdf"%(name))
            print("文件夹不为空")
        else:
            #pass
            print("文件夹为空")


