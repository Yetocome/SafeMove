from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from mapshow.views import safemap

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/') # Django内部的函数，用于解析URL，并将其映射到响应的视图函数上。

        self.assertEqual(found.func, safemap) # 检查解析网站根路径“/“时，能否找到名为home_page的函数

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = safemap(request)

        expected_html = render_to_string('safemap.html', request = request)    # To get the csrf token to work when using render_to_string,
                                                                            # you need to supply the request object so that the context
                                                                            # processors run.

        self.assertEqual(response.content.decode(), expected_html)  # 将response.content中的字节转换成Python中的Unicode字符串，
                                                                    # 这样就可以对比字符串，而不用像之前那样对比字节
