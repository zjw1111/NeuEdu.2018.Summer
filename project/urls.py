"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from diaries.views import *
from registration.backends.hmac.views import RegistrationView

urlpatterns = [
    # TODO: Please add captcha,registration back end here.
    url(r'^admin/', include(admin.site.urls)),
    # TODO: Use this way will increase an additional param <'index' or ''>
    # url(r'^(index|)$', index),
    url(r'^index$', index),
    url(r'^$', index),
    url(r'^login$', login),
    url(r'^logout$', logout),
    url(r'^userinfo$', userinfo),
    url(r'^post$', posting),
    url(r'^accounts/register/$',
        RegistrationView.as_view(
            form_class=MyCustomUserForm
        ),
        name='registration_register',
        ),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^captcha/', include('captcha.urls')),

]
