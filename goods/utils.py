from django.db.models import Q
from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    SearchHeadline,
)
from goods.models import Products


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))

    # эта конфигурация неплохо ищет
    vector = SearchVector("name", "description", config='russian')
    query = SearchQuery(query, config='russian')
    result = (
        Products.objects.annotate(search=vector, rank=SearchRank(vector, query))
        .filter(search=query).order_by('-rank')
    )

    result = result.annotate(
        headline=SearchHeadline(
            "name",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel="</span>",
        )
    )
    result = result.annotate(
        bodyline=SearchHeadline(
            "description",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel="</span>",
        )
    )

    return result

    # return Products.objects.filter(description__search=query)  # такой лукап доступен при подключении
    # полнотекстового поиска

    # keyword = [word for word in query.split() if len(word) > 2]
    #
    # q_objects = Q()
    # for token in keyword:
    #     q_objects |= Q(description__icontains=token)
    #     q_objects |= Q(name__icontains=token)
    #
    # return Products.objects.filter(q_objects)

#  products = Products.objects.filter(Q(name__icontains='Диван') | Q(description__icontains='Диван'))
