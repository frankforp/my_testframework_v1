#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/2/2017 5:03 PM
# @Author  : Winnichen
# @File    : LoginPage.py
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import os,time

class LoginPage(BasePage):
    username1_loc=(By.ID,"cred_userid_inputtext")
    login_loc=(By.ID,"cred_sign_in_button")
    password_loc=(By.ID,"passwordInput")
    submit_loc=(By.ID,"submitButton")
    checkpoint_loc=(By.CSS_SELECTOR,"#header-bar > div.heard-btn > div > a")
    logout_loc=(By.CSS_SELECTOR,"#header-bar > div.heard-btn > div > ul > li > a")
    checkpoint_logout_loc=(By.ID,"login_workload_logo_text")

    def input_username(self,username):
        #self.find_element(*self.username1_loc).send_keys(username)
        self.send_keys(self.username1_loc,username)

    def click_login(self):
        time.sleep(1)
        self.find_element(*self.login_loc).click()

    def input_password(self,password):
        #self.find_element(*self.password_loc).send_keys(password)
        self.send_keys(self.password_loc,password)

    def click_submit(self):
        time.sleep(1)
        self.find_element(*self.submit_loc).click()

    def get_username(self):
        return self.find_element(*self.checkpoint_loc).text

    def click_username(self):
        time.sleep(1)
        self.find_element(*self.checkpoint_loc).click()

    def click_logout(self):
        time.sleep(1)
        self.find_element(*self.logout_loc).click()



