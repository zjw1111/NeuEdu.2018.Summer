from django.contrib import admin
from models import *
#TODO: Please add your data model here.

#TODO: Please create a admin display configuration class here.

#TODO: Please register your data models


class DiaryAdmin(admin.ModelAdmin):
    list_display = ('user', 'budget', 'weight', 'date')
    search_fields = ('budget', 'weight', 'note')
    ordering = ('-date',)


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('username', 'height', 'gender', 'personal_page_url')
    fields = ('username', 'first_name', 'last_name', 'email', 'height', 'gender', 'personal_page_url')


admin.site.register(Diary, DiaryAdmin)
admin.site.register(UserInfo, UserInfoAdmin)
