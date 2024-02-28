from django.shortcuts import render, redirect

from carts.models import Cart
from goods.models import Products


def cart_add(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        # если продукт уже в корзине, то увеличим на 1 его количество
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)

    return redirect(request.META.get('HTTP_REFERER'))
    # else:
    #     carts = Cart.objects.filter(
    #         session_key=request.session.session_key, product=product)
    #
    #     if carts.exists():
    #         cart = carts.first()
    #         if cart:
    #             cart.quantity += 1
    #             cart.save()
    #     else:
    #         Cart.objects.create(
    #             session_key=request.session.session_key, product=product, quantity=1)
    #
    # user_cart = get_user_carts(request)
    # cart_items_html = render_to_string(
    #     "carts/includes/included_cart.html", {"carts": user_cart}, request=request)
    #
    # response_data = {
    #     "message": "Товар добавлен в корзину",
    #     "cart_items_html": cart_items_html,
    # }
    #
    # return JsonResponse(response_data)


def cart_change(request):
    pass


def cart_remove(request):
    pass
