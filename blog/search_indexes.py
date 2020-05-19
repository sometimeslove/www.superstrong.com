#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: superstrongz
@license: MIT Licence 
@contact: 857508399@qq.com
@site: http://www.superstrongz.com/
@software: PyCharm
@file: search_indexes.py
@time: ??
"""
from haystack import indexes
from django.conf import settings
from blog.models import Article, Category, Tag


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='author')

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(status='p')
