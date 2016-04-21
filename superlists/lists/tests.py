#_*_ coding:utf-8 _*_
from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page

class HomePageTest(TestCase):
    def test_root_resolves_to_home_page_view(self):
#解析url
        found = resolve('/')
        self.assertEqual(found.func,home_page)
