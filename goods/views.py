from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404

from goods.models import Products
from goods.utils import q_search


def catalog(request, category_slug=None):

    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if category_slug == 'all':
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)

    else:
        # ВАЖНО получение slug по внешнему ключу
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    if on_sale:
        goods = goods.filter(discount__gt=0)  # скидка больше 0

    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 3)
    current_page = paginator.page(page)  # int(page) без этого тоже робит пока

    context = {
        'title': 'Home - каталог',
        'goods': current_page,  # раньше тут была goods, до пагинации
        'slug_url': category_slug,
    }
    return render(request, 'goods/catalog.html', context)


def product(request, slug):
    product_ = Products.objects.get(slug=slug)
    context = {
        'product': product_
               }
    return render(request, 'goods/product.html', context)


