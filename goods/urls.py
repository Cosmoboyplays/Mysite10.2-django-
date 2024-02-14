from goods import views
from django.urls import path

app_name = 'catalog'

urlpatterns = [
    path('search/', views.catalog, name='search'),
    path('<slug:category_slug>/', views.catalog, name='index'),
    path('product/<slug:slug>/', views.product, name='product')
    ]