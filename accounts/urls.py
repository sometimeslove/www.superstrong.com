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

from django.conf.urls import url
from django.contrib.auth import views as auth_view

from . import views
from .forms import LoginForm

app_name="accounts"

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(success_url='/'), name='login', kwargs={'authentication_form': LoginForm}),
    url(r'^register/$', views.RegisterView.as_view(success_url="/"), name='register'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout')
]
