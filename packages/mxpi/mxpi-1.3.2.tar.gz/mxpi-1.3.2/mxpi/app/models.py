from django.db import models
from django.utils import timezone

# Create your models here.
class Mxpi_SArduino_in(models.Model):
    data = models.CharField(max_length=1000)
    publish = models.DateTimeField(default=timezone.now)  #建立一个发布时间的字段

    class Meta:
        ordering = ("-publish",) #规定按照publish倒序显示

class Mxpi_SArduino_out(models.Model):
    data = models.CharField(max_length=1000)
    publish = models.DateTimeField(default=timezone.now)  #建立一个发布时间的字段

    class Meta:
        ordering = ("-publish",) #规定按照publish倒序显示