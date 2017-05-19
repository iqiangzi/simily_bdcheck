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

    # 定位每页显示按钮
    paging_button_lco=(By.ID,"sel")
    # 每页显示10
    paging_button10_lco=(By.ID,"10")
    # 每页显示20
    paging_button20_lco=(By.ID,"20")
    # 每页显示50
    paging_button50_lco=(By.ID,"50")
    # 定位 记录总条数
    pageSum_loc=(By.XPATH,"html/body/div[4]/div[2]/form[2]/p/span[1]/b")
    # 选择每页显示10条后，返回列表的序号10
    select10_num_loc=(By.XPATH,"html/body/div[4]/div[2]/table/tbody/tr[11]/td[2]")
    # 选择每页显示20条后，返回列表的序号20
    select20_num_loc=(By.XPATH,"html/body/div[4]/div[2]/table/tbody/tr[21]/td[2]")
    # 选择每页显示50条后，返回列表的序号50
    select50_num_loc=(By.XPATH,"html/body/div[4]/div[2]/table/tbody/tr[51]/td[2]")
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
    page10Num_loc=(By.XPATH,"html/body/div[4]/div[2]/table/tbody/tr[11]/td[2]")

    # 定位 简明报告1.0
    simpleReport1_loc=(By.XPATH,"html/body/div[4]/div[2]/table/tbody/tr[2]/td[8]/a[2]")
    # 定位 简明报告2.0
    simpleReport2_loc=(By.XPATH,"html/body/div[4]/div[2]/table/tbody/tr[2]/td[8]/a[1]")
    # 定位 详细报告1.0
    detailReport1_loc=(By.XPATH,"html/body/div[4]/div[2]/table/tbody/tr[2]/td[8]/a[4]")
    # 定位 详细报告2.0
    detailReport2_loc=(By.XPATH,"html/body/div[4]/div[2]/table/tbody/tr[2]/td[8]/a[3]")
    # 定位 全文报告1.0
    fullReport1_loc=(By.XPATH,"html/body/div[4]/div[2]/table/tbody/tr[2]/td[8]/a[5]")



    def clickSimpleReport1(self):
        '''简明报告1.0，进行下载'''
        self.find_element(*self.simpleReport1_loc).click()

    def clickSimpleReport2(self):
        '''简明报告2.0，进行下载'''
        self.find_element(*self.simpleReport2_loc).click()

    def clickDetailReport1(self):
        '''详细报告1.0，进行下载'''
        self.find_element(*self.detailReport1_loc).click()

    def clickDetailReport2(self):
        '''详细报告2.0，进行下载'''
        self.find_element(*self.detailReport2_loc).click()

    def clickFullReport1(self):
        '''全文报告1.0，进行下载'''
        self.find_element(*self.fullReport1_loc).click()

    def clickFileTitle1(self):
        '''点击检索到的第一条记录的篇名，下载检测文章'''
        self.find_element(*self.resultList_fileTitle1_loc).click()

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

    #判断文件夹是否为空，不为空则重命名同名文件，以保证新下载的文件的唯一性。为空则直接下载
    def renameFileName(self):
        name=time.strftime("%Y-%m-%d %H_%M_%S")
        dir_path=GetPath().getAbsoluteDirPath("downloadFiles")
        if os.listdir(dir_path):
            #text=self.paperName()
            os.rename(dir_path+"/李硕.doc",dir_path+r"\%s.doc"%(name))
        else:
            pass

    def verifyExist1(self):
        #判断是否下载到本地,返回bool类型的True或False
        #判断文件是否存在
        dir_path=GetPath().getAbsoluteDirPath("downloadFiles")
        flag = os.path.exists(dir_path+"\李硕.doc")
        return flag



