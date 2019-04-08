from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class userFormReg(UserCreationForm):
    email = forms.EmailField()

    # name = forms.CharField(label='имя', max_length=100)
    # pass1 = forms.CharField(label='пароль', widget=forms.PasswordInput)
    # pass2 = forms.CharField(label='подтвердить пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
