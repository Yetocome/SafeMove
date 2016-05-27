from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from mapshow.views import safemap
from mapshow.models import UserEvent

# Create your tests here.
class SafeMapPageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/') # Django内部的函数，用于解析URL，并将其映射到响应的视图函数上。
        self.assertEqual(found.func, safemap) # 检查解析网站根路径“/“时，能否找到名为home_page的函数

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'safemap.html')

class UserEventModelTest(TestCase):

    def test_upload_and_saving_items(self):
        first_event = UserEvent()
        
        first_event.save()

        second_event = UserEvent()

        second_event.save()

        saved_events = UserEvent.objects.all()
        self.assertEqual(saved_events.count(), 2)

        first_saved_event = saved_events[0]
        second_saved_event = saved_events[1]
        self.assertEqual(0,0)

class UserEventUploadTest(TestCase):

    def test_upload_template(self):
        response = self.client.get('/uploadevent/')
        self.assertTemplateUsed(response, 'uploadevent.html')

    def test_medium_page_redirect_after_POST(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST[''] = ''
