#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-04-28 10:01:51
# @Author  : Nxy
# @Site    : 
# @File    : run_accountManagement.py
# @Software: PyCharm
from selenium import  webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
import time
from testCase.models import myUnitChrome
from testCase.models import myUnitFirefox

class RunAccountManagement(myUnitChrome.UnitChrome):
    def test_createChildAccount_run(self):
        pass
    def test_export_run(self):
        pass
    def test_operation_run(self):
        pass
    def test_accountlink_run(self):
        pass
