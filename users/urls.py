from users import views
from django.urls import path

app_name = 'user'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('users-cart/', views.users_cart, name='users-cart'),
    ]