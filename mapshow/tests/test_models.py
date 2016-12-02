# -*- coding: utf-8 -*-
from django.test import TestCase

from mapshow.models import *

# Create your tests here.


class UserEventModelTest(TestCase):

    def test_upload_and_saving_items(self):
        first_event = VisitorEvent()
        first_event.name = '王新澳'
        first_event.phone_number = '18888888888'
        first_event.age = 20
        first_event.email = '88888888@vip.com'
        first_event.event_type = 0
        first_event.save()

        second_event = VisitorEvent()
        second_event.name = '王澳新'
        second_event.phone_number = '16666666666'
        second_event.age = 20
        second_event.email = '666666@vip.com'
        second_event.event_type = 1
        second_event.save()

        saved_events = VisitorEvent.objects.all()
        self.assertEqual(saved_events.count(), 2)

        first_saved_event = saved_events[0]
        second_saved_event = saved_events[1]

        self.assertEqual(first_saved_event.name, '王新澳')
        self.assertEqual(first_saved_event.phone_number, '18888888888')
        self.assertEqual(first_saved_event.age, 20)
        self.assertEqual(first_saved_event.email, '88888888@vip.com')
        self.assertEqual(first_saved_event.event_type, 0)

        self.assertEqual(second_saved_event.name, '王澳新')
        self.assertEqual(second_saved_event.phone_number, '16666666666')
        self.assertEqual(second_saved_event.age, 20)
        self.assertEqual(second_saved_event.email, '666666@vip.com')
        self.assertEqual(second_saved_event.event_type, 1)



# 项目便签
# 1. 时间的数据库支持
# 2. 位置的数据库支持
# 3. 案件类型的数据库测试
