from django.db import models

# Create your models here.
class VisitorEvent(models.Model):
    name = models.TextField(default='', max_length = 30)
    phone_number = models.TextField(default='', max_length = 15) # +** ***********
    age = models.IntegerField(default=0)
    description = models.TextField(default='')
    email = models.TextField(default='')
    event_type = models.IntegerField(default=0)

    # 使用.objects.get()方法查询出来的结果将会包括姓名信息，admin中也是这样
    def __str__(self):
        return self.name
