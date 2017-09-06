#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/23/2017 3:25 PM
# @Author  : Winnichen
# @File    : conftest.py
def pytest_addoption(parser):
    parser.addoption("--settings", action="store", default="config.settings_stage",
                     help="Please pass a settings file")
    parser.addoption("--browser", action="store", default="chrome",
                 help="Please pass a browser(chrome,ie,firefox)")