#_*_ encoding: utf-8 *_*
from django import forms
from diaries.models import *
from captcha.fields import CaptchaField
from registration.forms import RegistrationForm
from django.contrib.auth.models import User

#TODO: Please design the extra user profile registration form.
#TODO: The extra user profile data will include height, gender, personal page url.


#TODO: Please design the login form.
class LoginForm(forms.Form):
    username = forms.CharField(label='User name', max_length=20)
    password = forms.CharField(label='Password', max_length=20, widget=forms.PasswordInput())



#TODO: Please design a date selection widget which might be a child class of forms.DateInput

#TODO: Please design the diary addition form, which should include budget, weight, note, date