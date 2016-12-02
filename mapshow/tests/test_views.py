# -*- coding: utf-8 -*-
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from mapshow.views import safemap, upload_event
from mapshow.models import *

class SafeMapPageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/') # Django内部的函数，用于解析URL，并将其映射到响应的视图函数上。
        self.assertEqual(found.func, safemap) # 检查解析网站根路径“/“时，能否找到名为home_page的函数

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'safemap.html')

class UserEventUploadTest(TestCase):

    def test_upload_template(self):
        response = self.client.get('/upload_event/')
        self.assertTemplateUsed(response, 'upload_event.html')

    def test_medium_page_redirect_after_POST(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['name']  = '王新澳'
        request.POST['phone_number'] = '18888888888'
        request.POST['email'] = '88888888@vip.com'
        request.POST['event_type'] = 0
        request.POST['description'] = '被打了'
        response = upload_event(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

        first_saved_event = VisitorEvent.objects.all()[0] #

        self.assertEqual(first_saved_event.name, '王新澳')
        self.assertEqual(first_saved_event.phone_number, '18888888888')
        self.assertEqual(first_saved_event.email, '88888888@vip.com')
        self.assertEqual(first_saved_event.event_type, 0)
        self.assertEqual(first_saved_event.description, '被打了')

    def test_multi_upload_100(self):
        pass
