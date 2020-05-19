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
from . import views

app_name = "comments"
urlpatterns = [
    # url(r'^po456stcomment/(?P<article_id>\d+)$', views.CommentPostView.as_view(), name='postcomment'),
    path('article/<int:article_id>/postcomment', views.CommentPostView.as_view(), name='postcomment'),
]
