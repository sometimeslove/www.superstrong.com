#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: superstrongz
@license: MIT Licence
@contact: 857508399@qq.com
@site: http://www.superstrongz.com/
@software: PyCharm
@file: feed.py
@time: ??
"""

from django.contrib.syndication.views import Feed
from blog.models import Article
from django.conf import settings
from django.utils.feedgenerator import Rss201rev2Feed
from DjangoBlog.utils import CommonMarkdown
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from DjangoBlog.utils import get_current_site


class DjangoBlogFeed(Feed):
    feed_type = Rss201rev2Feed

    description = '大巧无工,重剑无锋.'
    title = "且听风吟 大巧无工,重剑无锋. "
    link = "/feed/"

    def author_name(self):
        return get_user_model().objects.first().nickname

    def author_link(self):
        return get_user_model().objects.first().get_absolute_url()

    def items(self):
        return Article.objects.order_by('-pk')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return CommonMarkdown.get_markdown(item.body)

    def feed_copyright(self):
        # print(get_current_site().name)
        return "Copyright© 2018 且听风吟"

    def item_link(self, item):
        return item.get_absolute_url()

    def item_guid(self, item):
        return
