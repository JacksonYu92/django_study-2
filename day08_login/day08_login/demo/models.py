from django.db import models

class UserInfo(models.Model):
    # id = models.AutoField()
    name = models.CharField(verbose_name="姓名", max_length=16)
    age = models.IntegerField(verbose_name="年龄")
    email = models.CharField(verbose_name="邮箱", max_length=32)