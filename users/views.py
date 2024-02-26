from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)  # проверяет есть ли в базе
            if user:
                auth.login(request, user)
                messages.success(request, f"{request.user.username}, Вы вошли в аккаунт")
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Home - Авторизация',
        'form': form
    }
    return render(request, 'login.html', context)

# Таким образом, метод non_field_errors появляется после вызова  is_valid() , когда форма содержит ошибки,
# не связанные с конкретными полями, и позволяет обращаться к этим ошибкам для их обработки.


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()  # сохраняем в базе
            user = form.instance
            auth.login(request, user)
            messages.success(request, f"{user.username}, Вы зарегистрированы")
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Home - Регистрация',
        'form': form
    }
    return render(request, 'registration.html', context)


@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)  # чтобы форма могла принять ф
        if form.is_valid():
            form.save()  # сохраняем в базе
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)
    context = {
        'title': 'Home - Кабинет',
        'form': form,
        # 'orders': orders,
    }
    return render(request, 'profile.html', context)


@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('main:index'))


def users_cart(request):
    return render(request, 'users_cart.html')

