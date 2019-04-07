from django.contrib import admin
from .models import *


class DiaryAdmin(admin.ModelAdmin):
    list_display = ('user', 'budget', 'weight', 'date')
    search_fields = ('budget', 'weight', 'note')
    ordering = ('-date',)


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'height', 'gender', 'personal_page_url')
    fields = ('user', 'height', 'gender', 'personal_page_url')


admin.site.register(Diary, DiaryAdmin)
admin.site.register(UserInfo, UserInfoAdmin)
