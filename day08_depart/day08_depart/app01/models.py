from django.db import models

# Create your models here.
class Department(models.Model):
    title = models.CharField(verbose_name="标题", max_length=32)
    count = models.IntegerField(verbose_name="人树")