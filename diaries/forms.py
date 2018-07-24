#_*_ encoding: utf-8 *_*
from django import forms
from diaries.models import *
from captcha.fields import CaptchaField
from registration.forms import RegistrationForm
from django.contrib.auth.models import User


#TODO: Please design the extra user profile registration form.
#TODO: The extra user profile data will include height, gender, personal page url.
class ProfileForm(forms.Form):
    pass


#TODO: Please design the login form.
class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=20)
    password = forms.CharField(label='密　码', max_length=20, widget=forms.PasswordInput())


#TODO: Please design a date selection widget which might be a child class of forms.DateInput
class DateWidget(forms.DateInput):
    input_type = 'date'


#TODO: Please design the diary addition form, which should include budget, weight, note, date
class NewDiaryForm(forms.ModelForm):
    # captcha = CaptchaField()

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
        # self.fields['captcha'].label = '请输入图形中文字'

    def as_p(self):
        """
        Override the parent method, to make the HTML beautiful
        Returns this form rendered as HTML <p>s.
        """
        return self._html_output(
            normal_row='<p%(html_class_attr)s>%(label)s<br/>%(field)s%(help_text)s</p>',
            error_row='%s',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True)
