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
    # 进入信息管理后，面包屑：信息管理
    in_information_loc=(By.XPATH,"html/body/div[4]/div[2]/div/span[2]/b")

    # 查询按钮
    query_button_loc=(By.XPATH,".//*[@id='searchTaskForm']/div/input")
    # 检索条件 -- 账户 -- 下拉选择框
    #query_account_loc=(By.XPATH,".//*[@id='userIdSelect']")
    query_account_loc=(By.XPATH,".//*[@id='userIdSelectArrow']")
    # 选择检索条件 -- 账户 -- 下拉选择框 第一个元素
    query_account01_loc=(By.XPATH,".//*[@id='userIdUl']/li[1]")
    # 选择检索条件 -- 账户 -- 下拉选择框 第二个元素
    query_account02_loc=(By.XPATH,".//*[@id='userIdUl']/li[2]")
    # 检索条件 -- 任务名称 -- 输入框
    query_taskname_loc=(By.ID,"taskNameInput")
    # 检索条件 -- 创建时间（开始） -- 图标
    query_begintimeImg_loc=(By.CSS_SELECTOR,"img.ui-datepicker-trigger")
    #query_begintimeImg_loc=(By.XPATH,".//*[@id='searchTaskForm']/div/span[4]/img")
    # 检索条件 -- 创建时间（开始） -- 2017.05.05
    query_begintime_loc=(By.LINK_TEXT,"8")
    # 检索条件 -- 创建时间（结束） -- 图标
    query_endtimeImg_loc=(By.XPATH,".//*[@id='searchTaskForm']/div/span[5]/img")
    #query_endtimeImg_loc=(By.XPATH,"(//img[@alt='...'])[2]")
    # 检索条件 -- 创建时间（结束） -- 2017.05.31
    query_endtime_loc=(By.LINK_TEXT,"31")

    # 没有检索到符合检索条件的记录，提示：没有找到您要搜索的任务。
    query_isNull_loc=(By.XPATH,"html/body/div[4]/div[2]/p")
    # 输入检索条件后，检索结果列表第一条记录的账户
    query_firstAccount_loc=(By.XPATH,"html/body/div[4]/div[2]/table/tbody/tr[2]/td[2]")
    # 输入检索条件后，检索结果列表第一条记录的任务名
    query_firstName_loc=(By.XPATH,"html/body/div[4]/div[2]/table/tbody/tr[2]/td[3]/a")
    # 进入任务检测结果页面-面包屑-任务检测结果
    detectResult_page_loc=(By.XPATH,"html/body/div[4]/div[2]/div[1]/span[3]/b")

    # 定位每页显示按钮
    paging_button_lco=(By.ID,"sel")
    # 每页显示10
    paging_button10_lco=(By.ID,"10")
    # 每页显示20
    paging_button20_lco=(By.ID,"20")
    # 每页显示50
    paging_button50_lco=(By.ID,"50")
    # 定位记录总条数
    collegePage_sum_loc=(By.XPATH,"html/body/div[4]/div[2]/form[2]/p/span[1]/b")
    # 选择每页显示10条后，返回列表的序号10
    select10_num_loc=(By.XPATH,"html/body/div[4]/div[2]/table/tbody/tr[11]/td[1]")
    # 选择每页显示20条后，返回列表的序号20
    select20_num_loc=(By.XPATH,"html/body/div[4]/div[2]/table/tbody/tr[21]/td[1]")
    # 选择每页显示50条后，返回列表的序号50
    select50_num_loc=(By.XPATH,"html/body/div[4]/div[2]/table/tbody/tr[51]/td[1]")
    # 位于首页时，定位下一页按钮
    nextPage_button_loc=(By.XPATH,"html/body/div[4]/div[2]/form[2]/p/a[8]")
    # 位于首页时，定位尾页按钮
    lastPage_button_lco=(By.XPATH,"html/body/div[4]/div[2]/form[2]/p/a[9]")
    # 位于尾页时，定位上一页按钮
    previousPage_button_lco=(By.XPATH,"html/body/div[4]/div[2]/form[2]/p/a[2]")
    # 位于尾页时，定位首页按钮
    firstPage_button_lco=(By.XPATH,"html/body/div[4]/div[2]/form[2]/p/a[1]")
    # 首页、下一页、上一页、尾页都存在时，定位尾页
    lastPage1_button_lco=(By.XPATH,"html/body/div[4]/div[2]/form[2]/p/a[11]")
    # 首页、下一页、上一页、尾页都存在时，定位下一页
    nextPage1_button_loc=(By.XPATH,"html/body/div[4]/div[2]/form[2]/p/a[10]")
    # 定位 每页显示10条时，当前列表最后一条的序号
    page10Num_loc=(By.XPATH,"html/body/div[4]/div[2]/table/tbody/tr[11]/td[1]")


    def clickNextPage(self):
        '''在首页时，点击下一页按钮'''
        self.find_element(*self.nextPage_button_loc).click()

    def clickNextPage1(self):
        '''首页、尾页都存在时，点击下一页按钮'''
        self.find_element(*self.nextPage1_button_loc).click()

    def clickLastPage(self):
        '''在首页时，点击尾页按钮'''
        self.find_element(*self.lastPage_button_lco).click()

    def clickFirstPage(self):
        '''在尾页时，点击首页按钮'''
        self.find_element(*self.firstPage_button_lco).click()

    def clickPreviousPage(self):
        '''在尾页时，点击上一页按钮'''
        self.find_element(*self.previousPage_button_lco).click()

    def returnFirstPage(self):
        '''在尾页时，返回首页两个字'''
        return self.find_element(*self.firstPage_button_lco).text

    def returnLastPage(self):
        '''在首页时，返回尾页两个字'''
        return self.find_element(*self.lastPage_button_lco).text

    def returnNowPageNum(self):
        '''每页显示10条时，当前列表最后一条数据的序号'''
        return self.find_element(*self.page10Num_loc).text

    def inInfoManage(self):
        # 进入管理中心--信息管理
        # 该方法不可用，悬浮不行，直接输入url进入
        '''鼠标悬停在管理中心，然后点击信息管理'''
        above=self.find_element(*self.manageCenter_button_loc)
        ActionChains(self.driver).move_to_element(above).perform()
        # 悬浮后，点击信息管理
        sleep(5)
        self.find_element(*self.information_button_loc).click()

    def inInfoManageCrumbs(self):
        '''返回信息管理页面的面包屑：信息管理'''
        crumbs=self.find_element(*self.in_information_loc).text
        return crumbs

    def accountSelectLi1(self):
        '''选择检索条件 -- 账户 -- 下拉选择框 第一个元素'''
        self.find_element(*self.query_account_loc).click()
        sleep(2)
        self.find_element(*self.query_account01_loc).click()
        #query_account01_loc=account.find_element_by_id("collegecheck").click

    def accountSelectLi2(self):
        '''选择检索条件 -- 账户 -- 下拉选择框 第二个元素'''
        self.find_element(*self.query_account_loc).click()
        sleep(2)
        self.find_element(*self.query_account02_loc).click()
        #query_account01_loc=account.find_element_by_id("collegecheck.songp").click

    def queryButtonClick(self):
        '''点击查询按钮'''
        self.find_element(*self.query_button_loc).click()

    def inputTaskName(self,taskName):
        '''输入任务名称检索条件，进行检索'''
        self.find_element(*self.query_taskname_loc).clear()
        self.find_element(*self.query_taskname_loc).send_keys(taskName)

    def queryFirstAccountName(self):
        '''输入检索条件后，返回检索结果列表第一条记录的账户名'''
        firstAccount=self.find_element(*self.query_firstAccount_loc).text
        return firstAccount

    def queryFirstTaskName(self):
        '''输入检索条件后，返回检索结果列表第一条记录的任务名'''
        firstName=self.find_element(*self.query_firstName_loc).text
        return firstName

    def queryIsNull(self):
        '''没有检索到复合检索条件的记录，返回提示信息“没有找到您要搜索的任务。”'''
        message=self.find_element(*self.query_isNull_loc).text
        return message

    # 返回总的信息条数
    def pageMsg(self):
        pagenum=self.find_element(*self.collegePage_sum_loc).text
        return pagenum

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

    def inDetectResult(self):
        '''信息管理页面，点击检测结果中第一条记录的任务名，进入任务检测结果页面。
        返回任务检测结果页面的面包屑：任务检测结果
        '''
        self.find_element(*self.query_firstName_loc).click()
        sleep(2)
        result=self.find_element(*self.detectResult_page_loc).text
        return result

    def pagingButtonSelect10(self):
        '''点击每页显示页数按钮，选择每页显示10条'''
        self.find_element(*self.paging_button_lco).click()
        self.find_element(*self.paging_button10_lco).click()

    def pagingButtonSelect20(self):
        '''点击每页显示页数按钮，选择每页显示20条'''
        self.find_element(*self.paging_button_lco).click()
        self.find_element(*self.paging_button20_lco).click()

    def pagingButtonSelect50(self):
        '''点击每页显示页数按钮，选择每页显示50条'''
        self.find_element(*self.paging_button_lco).click()
        self.find_element(*self.paging_button50_lco).click()

    def pagingSelect10Result(self):
        '''选择每页显示10条后，返回列表的序号10'''
        result=self.find_element(*self.select10_num_loc).text
        return result

    def pagingSelect20Result(self):
        '''选择每页显示20条后，返回列表的序号20'''
        result=self.find_element(*self.select20_num_loc).text
        return result

    def pagingSelect50Result(self):
        '''选择每页显示50条后，返回列表的序号50'''
        result=self.find_element(*self.select50_num_loc).text
        return result






