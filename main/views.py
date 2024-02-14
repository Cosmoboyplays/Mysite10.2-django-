from django.shortcuts import render

from goods.models import Categories


def index(request):

    context = {'title': 'home',
               'content': 'Магазин мебели HOME',
               }
    return render(request, "main/index.html", context)


def about(request):
    context = dict(title='О нас',
                   content='О нас',
                   text_on_page="Много много много текста о нас, какие мы крутые, что нас отличает,"
                                " какие мы все тут особенные и классные")
    return render(request, 'main/about.html', context)




# Create your views here.
