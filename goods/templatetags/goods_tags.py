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
    передается в функцию при вызове из шаблона.

    Таким образом, при вызове функции в шаблоне href="?{% change_params page=page %}", объект контекста автоматически
    передается в функцию change_params как параметр context, и значение GET-параметра page из контекста также
    передается в функцию в качестве kwargs.
    """
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)
