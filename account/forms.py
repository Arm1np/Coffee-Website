from tkinter.tix import Form
from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Enter your first name"}))

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Enter your last name"}))

    username = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Enter your username"}))

    email = forms.EmailField(widget=forms.EmailInput())

    password = forms.CharField(widget=forms.PasswordInput())

    re_password = forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data.get('username')

        exists_user = User.objects.filter(username=username).exists()

        if exists_user:
            raise forms.ValidationError("this user has exists!!")

        return username

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        print(password)
        print(re_password)

        if password != re_password:
            raise forms.ValidationError('کلمه های عبور مغایرت دارند')

        return password

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Enter your username"}))

    password = forms.CharField(widget=forms.PasswordInput())
    
