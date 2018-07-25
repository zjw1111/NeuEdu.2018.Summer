# _*_ encoding: utf-8 *_*
from django import forms
from diaries.models import *
from captcha.fields import CaptchaField
from registration.forms import RegistrationForm
from django.contrib.auth.models import User


class MyCustomUserForm(RegistrationForm):
    captcha = CaptchaField()

    class Meta:
        model = UserInfo
        fields = ['username', 'email', 'password1', 'password2', 'gender', 'height', 'personal_page_url', 'captcha']

    def __init__(self, *args, **argv):
        RegistrationForm.__init__(self, *args, **argv)
        self.fields['username'].label = '* 用户名:'
        self.fields['email'].label = '* Email:'
        self.fields['password1'].label = '* 密码:'
        self.fields['password2'].label = '* 密码确认:'
        self.fields['captcha'].label = '* 验证码:'

    def as_table(self):
        """
        Override the parent method, to make the HTML beautiful
        Returns this form rendered as HTML <tr>s -- excluding the <table></table>.
        """
        return self._html_output(
            normal_row='<tr%(html_class_attr)s"><th>%(label)s</th><td>%(field)s%(help_text)s%(errors)s</td></tr>',
            error_row='<tr><td colspan="2">%s</td></tr>',
            row_ender='</td></tr>',
            help_text_html='<br /><span class="helptext">%s</span>',
            errors_on_separate_row=False)


class ProfileForm(forms.Form):
    gender = forms.ChoiceField(label='性别', choices=[(0, '男'), (1, '女')])
    height = forms.FloatField(label="身高(cm)", min_value=0)
    personal_page_url = forms.URLField(label='个人主页', max_length=300)

    def as_table(self):
        """
        Override the parent method, to make the HTML beautiful
        Returns this form rendered as HTML <tr>s -- excluding the <table></table>.
        """
        return self._html_output(
            normal_row='<tr%(html_class_attr)s height="45px"><th>%(label)s</th><td>%(errors)s%(field)s%(help_text)s</td></tr>',
            error_row='<tr><td colspan="2">%s</td></tr>',
            row_ender='</td></tr>',
            help_text_html='<br /><span class="helptext">%s</span>',
            errors_on_separate_row=False)


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=20)
    password = forms.CharField(label='密　码', max_length=20, widget=forms.PasswordInput())


class DateWidget(forms.DateInput):
    input_type = 'date'


class NewDiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ['note', 'budget', 'weight', 'date', 'user']

    def __init__(self, *args, **argv):
        forms.ModelForm.__init__(self, *args, **argv)
        self.fields['note'].label = '日记文本:'
        self.fields['budget'].label = '预算:'
        self.fields['weight'].label = '体重:'
        self.fields['date'].label = '日期:'
        self.fields['budget'].widget = forms.NumberInput(attrs={'min': 0, 'step': '0.1'})
        self.fields['weight'].widget = forms.NumberInput(attrs={'min': 0, 'step': '0.1'})
        self.fields['date'].widget = DateWidget()
        self.fields['user'].widget = forms.HiddenInput()