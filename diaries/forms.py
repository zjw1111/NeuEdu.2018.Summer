#_*_ encoding: utf-8 *_*
from django import forms
from diaries import models
#TODO: Please add your data model here.

from captcha.fields import CaptchaField
from registration.forms import RegistrationForm
from django.contrib.auth.models import User

#TODO: Please design the extra user profile registration form.
#TODO: The extra user profile data will include height, gender, personal page url.



#TODO: Please design the login form.


#TODO: Please design a date selection widget which might be a child class of forms.DateInput

#TODO: Please design the diary addition form, which should include budget, weight, note, date