import re
from typing import Type

from django.conf import settings
from django.db.models import Q
from rest_framework.request import Request
from rest_framework.views import APIView
from django.utils.translation import gettext_lazy as _
from rest_framework.serializers import ModelSerializer

from velait.common.exceptions import VelaitError
from velait.velait_django.main.models import BaseModel
from velait.velait_django.main.api.serializers import BaseSerializer
from velait.velait_django.main.api.responses import APIResponse
from velait.velait_django.main.api.pagination import VelaitPagination
from velait.velait_django.main.services.services import filter_objects
from velait.velait_django.main.services.search import SearchError, DjangoSearch


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


class IdsListingView(APIView):
    model: Type[BaseModel]
    serializer_class: Type[BaseSerializer]

    def get(self, request: Request):
        searched_ids = request.query_params.get('ids')

        if searched_ids is None:
            return APIResponse(errors={
                VelaitError(
                    name="query",
                    description=_("You must provide 'ids' query parameter to use this view"),
                )
            })
        elif len(searched_ids) > getattr(settings, 'ID_LISTING_MAX_LEN', 40000):
            return APIResponse(errors={
                VelaitError(
                    name="query",
                    description=_("Your 'ids' are too long. Try shortening them"),
                )
            })
        elif not re.match(
            r"([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})|(\d+),*",
            searched_ids,
        ):
            return APIResponse(errors={
                VelaitError(
                    name="query",
                    description=_("Your 'ids' must be either UUID or integers"),
                )
            })

        numerical_ids = list(int(searched_id) for searched_id in re.findall(r"\d+", searched_ids))
        uuids = re.findall(
            r"([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})",
            searched_ids,
        )

        return APIResponse(
            data=self.serializer_class(
                instance=filter_objects(
                    self.model.objects,
                    Q(id__in=numerical_ids) | Q(uuid__in=uuids),
                    limit=getattr(settings, "ID_LISTING_MAX_RESULTS", 300),
                ),
                many=True,
            ).data,
            status=200,
        )


__all__ = [
    'IdsListingView',
    'SearchView',
]
