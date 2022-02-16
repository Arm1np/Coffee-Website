from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from account.forms import RegisterForm, LoginForm

# Create your views here.


def register_user(request):
    # if request.user.is_authenticated:
    #     return redirect('/')
    register_form = RegisterForm(request.POST or None)

    if register_form.is_valid():
        first_name = register_form.cleaned_data.get('first_name')
        last_name = register_form.cleaned_data.get('last_name')
        username = register_form.cleaned_data.get('username')
        password = register_form.cleaned_data.get('password')
        email = register_form.cleaned_data.get('email')
        User.objects.create_user(first_name=first_name, last_name=last_name,
                                 username=username, email=email, password=password)
        return redirect('/login/')

    context = {
        'register_form': register_form
    }
    return render(request, 'account/register.html', context)


def login_user(request):
    login_form = LoginForm(request.POST or None)

    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')

    return render(request, 'account/login.html', {"login_form": login_form})

def logout_user(request):
    logout(request)
    return redirect('/')