# _*_ encoding: utf-8 _*_
from django.db import models
from django.contrib.auth.models import User, AbstractUser

#TODO: Please design the extra user profile data model which should be a extension of Django standard user profile, the extra data should include height, gender, personal page url.
class UserInfo(User):
    height = models.FloatField(verbose_name="身高")
    gender = models.IntegerField(choices=[(0, 'Woman'), (1, 'Man')], default=0, verbose_name="性别")
    personal_page_url = models.URLField(max_length=200, verbose_name="个人主页")

#TODO: Please design the data model which save the diary information. It should include the budget, weight, note, date.
class Diary(models.Model):
    budget = models.FloatField(verbose_name="预算")
    weight = models.FloatField(verbose_name="体重")
    note = models.TextField(verbose_name="日记文本")
    date = models.DateField(auto_now=True, verbose_name="日期")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户名")