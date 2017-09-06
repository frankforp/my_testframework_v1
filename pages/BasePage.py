#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/2/2017 3:26 PM
# @Author  : Winnichen
# @File    : BasePage.py
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time

class BasePage(object):
    def __init__(self, selenium_driver, base_url="", pagetitle=""):
        self.driver = selenium_driver
        self.base_url = base_url
        self.pagetitle = pagetitle

    def on_page(self, pagetitle):
        return pagetitle in self.driver.title

    def _open(self, url, pagetitle):
        self.driver.get(url)
        self.driver.maximize_window()
        assert self.on_page(pagetitle), u"Failed to open the url: %s"%url

    def open(self):
        self._open(self.base_url, self.pagetitle)

    def open_wait(self):
        try:
            self.driver.get(self.base_url)
            WebDriverWait(self.driver,120).until(EC.title_contains(self.pagetitle))
        except:
            logging.error("Failed to open url: "+self.base_url)
            assert 0,u"Failed to open the url: %s"%self.base_url

    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,60).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            logging.error(u"%s can not find the element %s"%(self, loc))
            assert 0,u"%s can not find the element: %s"%(self, loc)

    def switch_frame(self, loc):
        return self.driver.switch_to_frame(loc)

    def script(self, src):
        self.driver.execute_script(src)

    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            logging.error(u"%s can not find the element %s"%(self, loc))


