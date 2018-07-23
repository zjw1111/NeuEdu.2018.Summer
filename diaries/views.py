# _*_ encoding:utf-8 _*_
from django.core.mail import EmailMessage
from django.template import RequestContext
from django.template import Context, Template
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages
from diaries import models, forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def index(request, pid=None, del_pass=None):
    template = get_template('index.html')
    html = template.render(locals())
    return HttpResponse(html)
    #As the home page, should check the authenticaiton status first,
    #if already login then use the username query the diaries data.
    #check the message instance, if any, show it.

#user function decorator login_required to check whether or not it already login, if not, redirect to login page
def userinfo(request):
    pass
    #should check the authenticaiton status first,
    #if already login then use the username query the profile data.
    #if the form submit, check the validity of form data, if valid, save data and show success information.
    #if not, show error message.Please use the message mechanism.
    #if current access is the first time show page, then display the userinfo form.


def login(request):
    pass
    #should check the authenticaiton status first,if already login, redirect to home page.
    #if the form submit, check the validity of form data, if valid, use the username and password to perform
    # authentication. if the user is not valid or not been activated, then display the respective message.
    #if the user is valid, then login and display the success message.
    #if current access is the first time show page, then display the login form.

def logout(request):
    pass
    #logout current user.
    #Display the logout message.
    #redirect to home page.

#user function decorator login_required to check whether or not it already login, if not, redirect to login page
def posting(request):
    pass
    #should check the authenticaiton status first,if already login, get the username.
    #should display the message contents if any.
    # if the form submit, check the validity of form data, if valid, save the diary data and show success message.
    #Tips: should user the instance key parameter which specify the diary data model instance otherwise you cannot
    #save data.
    #if current access is the first time show page, then display the login form, and show a reminder message.
