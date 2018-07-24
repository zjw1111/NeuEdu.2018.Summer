# _*_ encoding:utf-8 _*_
from django.core.mail import EmailMessage
from django.template import RequestContext
from django.template import Context, Template
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages
from diaries.models import *
from diaries.forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def index(request, pid=None, del_pass=None):
    template = get_template('index.html')
    username = None
    if request.user.is_authenticated():
        username = request.user.username
        diaries = Diary.objects.filter(user=request.user).order_by('date')
    html = template.render(locals(), request)
    return HttpResponse(html)


@login_required
def userinfo(request):
    template = get_template('userinfo.html')
    username = request.user.username
    if UserInfo.objects.filter(username=username).exists():
        user = UserInfo.objects.get(username=username)
        gender = user.gender
        height = user.height
        personal_page_url = user.personal_page_url
    else:
        UserInfo.objects.create(user_ptr_id=request.user.id, gender=1, height=0, personal_page_url="")

    if request.method == 'GET':
        if 'modify' in request.GET and request.GET['modify'] == '1':
            profile_form = ProfileForm()
    else:
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            # username = auth.authenticate(request, username=loginform.cleaned_data['username'],
            #                              password=loginform.cleaned_data['password'])
            # if username and username.is_active:
            #     messages.add_message(request, messages.SUCCESS, '登录成功！%s，你好' % username)
            # else:
            #     username = None
            #     messages.add_message(request, messages.WARNING, '请检查你的用户名、密码')
            profile_form.save()
        else:
            # username = None
            messages.add_message(request, messages.WARNING, '2请检查你的用户名、密码')
    html = template.render(locals(), request)
    return HttpResponse(html)
    #should check the authenticaiton status first,
    #if already login then use the username query the profile data.
    #if the form submit, check the validity of form data, if valid, save data and show success information.
    #if not, show error message.Please use the message mechanism.
    #if current access is the first time show page, then display the userinfo form.


def login(request):
    template = get_template('login.html')
    username = None
    next = ""
    if request.user.is_authenticated():
        username = request.user.username
        return HttpResponseRedirect('/')
    else:
        if request.method == 'GET':
            loginform = LoginForm()
            if 'next' in request.GET:
                next = request.GET['next']
            else:
                next = '/'
        else:
            loginform = LoginForm(request.POST)
            if loginform.is_valid():
                username = auth.authenticate(request, username=loginform.cleaned_data['username'],
                                             password=loginform.cleaned_data['password'])
                if username and username.is_active:
                    messages.add_message(request, messages.SUCCESS, '登录成功！%s，你好' % username)
                    auth.login(request, username)
                    if 'next' in request.POST:
                        return HttpResponseRedirect(request.POST['next'])
                    else:
                        return HttpResponseRedirect('/')
                else:
                    username = None
                    messages.add_message(request, messages.WARNING, '请检查你的用户名、密码')
            else:
                username = None
                messages.add_message(request, messages.WARNING, '请检查你的用户名、密码')
    html = template.render(locals(), request)
    return HttpResponse(html)


def logout(request):
    auth.logout(request)
    messages.add_message(request, messages.INFO, '您已注销，欢迎再次登录!')
    return HttpResponseRedirect('/')


@login_required
def posting(request):
    template = get_template('posting.html')
    username = None
    user = None
    if request.method == 'GET':
        diary_form = NewDiaryForm()
        user = request.user.id
    else:
        diary_form = NewDiaryForm(request.POST)
        if diary_form.is_valid():
            diary_form.save()
            messages.add_message(request, messages.INFO, '新的日记提交成功！')
            return HttpResponseRedirect('/')
        else:
            messages.add_message(request, messages.WARNING, '日记提交失败，请检查')
    html = template.render(locals(), request)
    return HttpResponse(html)
    # should check the authenticaiton status first,if already login, get the username.
    # should display the message contents if any.
    # if the form submit, check the validity of form data, if valid, save the diary data and show success message.
    # Tips: should user the instance key parameter which specify the diary data model instance otherwise you cannot save data.
    # if current access is the first time show page, then display the login form, and show a reminder message.
