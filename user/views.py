from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from user.form import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from user.models import Profile


def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'user/register.html', context={'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        print(request.FILES)
        if not form.is_valid():
            return render(request, 'user/register.html', context={'form': form})
        password_confirm = form.cleaned_data.pop('password_confirm')
        image = form.cleaned_data.pop('image')
        user = User.objects.create_user(**form.cleaned_data)
        Profile.objects.create(user=user, image=image)
        return redirect('home')


def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, "user/login.html", context={'form': form})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, 'user/login.html', context={'form': form})
        user = authenticate(**form.cleaned_data)
        if user is None:
            form.add_error(None, "Username or password is incorrect.")
            return render(request, 'user/login.html', context={'form': form})
        login(request, user)
        return redirect('home')


def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return redirect('home')

@login_required(login_url='login')
def profile(request):
    posts = request.user.posts.all()
    return render(request,'user/profile.html', context={'posts': posts})
