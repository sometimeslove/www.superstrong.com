#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: superstrongz
@license: MIT Licence 
@contact: 857508399@qq.com
@site: http://www.superstrongz.com/
@software: PyCharm
@file: clear_cache.py
@time: ??
"""
from DjangoBlog.utils import cache
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'clear the whole cache'

    def handle(self, *args, **options):
        cache.clear()
        self.stdout.write(self.style.SUCCESS('Cleared cache\n'))
