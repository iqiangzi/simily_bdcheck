#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-04-28 10:01:52
# @Author  : Nxy
# @Site    : 
# @File    : run_informationManagement.py
# @Software: PyCharm
from selenium import  webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
import time
from testCase.models import myUnitChrome
from testCase.models import myUnitFirefox

class RunInformationManagement(myUnitChrome.UnitChrome):
    def test_taskNameLink_run(self):
        pass
    def test_delete_run(self):
        pass
