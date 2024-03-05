from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from carts.models import Cart
from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)  # проверяет есть ли в базе

            session_key = request.session.session_key  # узнаем ключ сессии до логина

            if user:
                auth.login(request, user)  # логиним
                messages.success(request, f"{request.user.username}, Вы вошли в аккаунт")

                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)  # меняем ключ сессии при логина

                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))

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

        session_key = request.session.session_key

        if form.is_valid():
            form.save()  # сохраняем в базе
            user = form.instance
            auth.login(request, user)
            messages.success(request, f"{user.username}, Вы зарегистрированы")

            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)  # меняем ключ сессии при регистрации

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

