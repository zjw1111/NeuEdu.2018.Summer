# _*_ encoding: utf-8 _*_
from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.FloatField(verbose_name="身高", null=True, blank=True)
    gender = models.IntegerField(choices=[(0, '男'), (1, '女')], default=0, verbose_name="性别", null=True, blank=True)
    personal_page_url = models.URLField(max_length=200, verbose_name="个人主页", null=True, blank=True)


class Diary(models.Model):
    budget = models.FloatField(verbose_name="预算")
    weight = models.FloatField(verbose_name="体重")
    note = models.TextField(verbose_name="日记文本")
    date = models.DateField(verbose_name="日期")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户名")