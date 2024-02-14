from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import UserLoginForm


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('hub:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Home - Авторизация',
        'form': form,
        # 'form': form
    }
    return render(request, 'login.html', context)


def registration(request):

    context = {
        'title': 'Home - Регистрация',
        # 'form': form
    }
    return render(request, 'registration.html', context)


def profile(request):
    context = {
        'title': 'Home - Кабинет',
        # 'form': form,
        # 'orders': orders,
    }
    return render(request, 'profile.html', context)


# def users_cart(request):
#     return render(request, 'users/users_cart.html')
#

@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('main:index'))
