from django.db import models

# Create your models here.
class UserEvent(models.Model):
    name = models.CharField(default='', max_length = 30)
    phone_number = models.CharField(default='', max_length = 15) # +** ***********
    age = models.IntegerField(default=0)
    description = models.TextField(default='')
    mail = models.TextField(default='')
    event_type = models.IntegerField(default=0)

    # 使用.objects.get()方法查询出来的结果将会包括姓名信息
    def __str__(self):
        return self.name
