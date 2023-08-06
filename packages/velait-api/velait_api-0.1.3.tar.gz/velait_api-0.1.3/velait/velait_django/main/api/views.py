from typing import Type

from rest_framework.views import APIView
from rest_framework.serializers import ModelSerializer

from velait.velait_django.main.models import BaseModel
from velait.velait_django.main.api.responses import APIResponse
from velait.velait_django.main.services.search import SearchError, DjangoSearch
from velait.velait_django.main.api.pagination import VelaitPagination


class SearchView(APIView):
    model: Type[BaseModel] = None
    serializer_class: Type[ModelSerializer] = None
    search_class: Type[DjangoSearch] = DjangoSearch

    def __init__(self, *args, **kwargs):
        super(SearchView, self).__init__(*args, **kwargs)

        if self.model is None or self.serializer_class is None:
            raise NotImplementedError("Model or Serializer were not supplied to the SearchView")

    def get_search_object(self):
        return self.search_class(
            search_=self.request.GET.get('search'),
            query=self.request.GET.get('query'),
            ordering=self.request.GET.get('ordering'),
            page=self.request.GET.get('page'),
            model=self.model,
            paginate=False,
        )

    def get(self, request, *args, **kwargs):
        try:
            search = self.get_search_object()
            paginator = VelaitPagination()
            queryset = paginator.paginate_queryset(queryset=search.search(), request=request, view=self)
            return paginator.get_paginated_response(self.serializer_class(instance=queryset, many=True).data)

        except SearchError as exc:
            return APIResponse(errors=[exc], status=400)
