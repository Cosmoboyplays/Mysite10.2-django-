from django import template
from django.utils.http import urlencode

from goods.models import Categories

register = template.Library()


@register.simple_tag()
def tag_categories():
    return Categories.objects.all()


@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    """Параметр context в функции change_params указывается как takes_context=True в декораторе
    @register.simple_tag. Это означает, что функция принимает объект контекста шаблона Django, который автоматически
    передается в функцию при вызове из шаблона. context из views.py будет тут

    Таким образом, при вызове функции в шаблоне href="?{% change_params page=page %}", объект контекста автоматически
    передается в функцию change_params как параметр context, и значение GET-параметра page из контекста также
    передается в функцию в качестве kwargs.
    """

    query = context['request'].GET.dict()  # какие еще ключи есть в словаре? Почему я не могу его распечатать обычным ?
    query.update(kwargs)
    return urlencode(query)

   '''Функция  urlencode  в Django используется для кодирования словаря параметров в строку запроса URL.
    Она принимает словарь параметров и возвращает строку, в которой каждый ключ-значение пара представлена 
    в формате  key=value  и разделена символом  & . Это удобно для создания строки запроса URL с параметрами
     для использования в ссылках или при передаче данных через GET-запросы. 
 
    Например, если у вас есть словарь параметров  {'page': 2, 'category': 'shoes'} , то вызов функции  urlencode  
    преобразует его в строку вида  'page=2&category=shoes' 
    '''