# _*_ encoding: utf-8 *_*
from django import forms
from diaries.models import *
from captcha.fields import CaptchaField
from registration.forms import RegistrationForm
from django.contrib.auth.models import User


# TODO: Please design the extra user profile registration form.
# TODO: The extra user profile data will include height, gender, personal page url.
class ProfileForm(forms.Form):
    gender = forms.ChoiceField(label='性别', choices=[(0, '男'), (1, '女')], widget=forms.RadioSelect())
    height = forms.FloatField(label="身高(cm)", min_value=0)
    # gender = forms.RadioSelect(choices=[(0, '女'), (1, '男')])
    personal_page_url = forms.CharField(label='个人主页', max_length=20)

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


# TODO: Please design the login form.
class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=20)
    password = forms.CharField(label='密　码', max_length=20, widget=forms.PasswordInput())


# TODO: Please design a date selection widget which might be a child class of forms.DateInput
class DateWidget(forms.DateInput):
    input_type = 'date'


# TODO: Please design the diary addition form, which should include budget, weight, note, date
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
