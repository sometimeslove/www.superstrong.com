#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: superstrongz
@license: MIT Licence 
@contact: 857508399@qq.com
@site: http://www.superstrongz.com/
@software: PyCharm
@file: urls.py
@time: ??
"""

from django.urls import path
from werobot.contrib.django import make_view
from .robot import robot

app_name = "servermanager"
urlpatterns = [
    path(r'robot', make_view(robot)),

]
