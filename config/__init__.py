#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/23/2017 2:58 PM
# @Author  : Winnichen
# @File    : __init__.py.py
import os
import importlib

import pytest

try:
    mod = pytest.config.getoption('--settings')
except AttributeError:
    mod = os.environ.get('MODULE', 'config.settings_stage')
settings = importlib.import_module(mod)