#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: superstrongz
@license: MIT Licence 
@contact: 857508399@qq.com
@site: http://www.superstrongz.com/
@software: PyCharm
@file: oauth_tags.py
@time: ??
"""
from oauth.oauthmanager import get_oauth_apps
from django.urls import reverse
from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag('oauth/oauth_applications.html')
def load_oauth_applications(request):
    applications = get_oauth_apps()
    if applications:
        baseurl = reverse('oauth:oauthlogin')
        path = request.get_full_path()

        apps = list(map(lambda x: (x.ICON_NAME,
                                   '{baseurl}?type={type}&next_url={next}'
                                   .format(baseurl=baseurl, type=x.ICON_NAME, next=path)), applications))
    else:
        apps = []
    return {
        'apps': apps
    }
