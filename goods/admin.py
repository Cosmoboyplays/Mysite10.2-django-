from django.contrib import admin
from goods.models import Categories, Products


# admin.site.register(Categories)  # регистрируем тут модель, чтобы в админке увидеть таблицы
# admin.site.register(Products)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}  # автозаполнение слага
    list_display = ['name']


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}  # тоже оно
    list_display = ['name', 'quantity', 'price', 'discount']
    list_editable = ['discount']
    search_fields = ['name', 'description']
    list_filter = ['discount', 'quantity', 'category']
    fields = ['name',
              'category',
              'slug',
              'description',
              'image',
              ('price', 'discount'),
              'quantity',
              ]

