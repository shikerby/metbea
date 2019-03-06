from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import Profile
from blog.models import Post


class MyAuthForm(AuthenticationForm):
    username = forms.CharField(label="登录用户名", widget=forms.TextInput(attrs={'placeholder': 'Account'}))
    password = forms.CharField(label="请输入密码", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label="用户注册",widget=forms.TextInput(attrs={'placeholder': '请输入用户名'}))
    email = forms.EmailField(label="邮箱", widget=forms.EmailInput(attrs={'placeholder': '请填写可用邮箱'}))
    password = forms.CharField(label="密码", widget=forms.PasswordInput(attrs={'placeholder': '输入密码'}))
    password2 = forms.CharField(label="重复密码", widget=forms.PasswordInput(attrs={'placeholder': '再输入一次'}))

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': '请输入新邮箱'}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')


class UserWritePostForm(forms.ModelForm):
    title = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': '请在写文章标题'}))
    slug = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': '为文章定义一个好看的url 例如: meet-django '}))
    # status = forms.MultipleChoiceField(label="文章状态", widget=forms.Select, choices=STATIC_CHOICES)
    body = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder': '请在此处写你的文章,可以使用markdown语法'}))
    class Meta:
        model = Post
        fields = ('title', 'slug', 'body')


class SetPostPublishTimeForm(forms.Form):
    pub_time = forms.DateTimeField(label='', widget=forms.DateTimeInput(attrs={'id': 'datetimepicker', 'placeholder': '点击选择精确发布时间'}))
