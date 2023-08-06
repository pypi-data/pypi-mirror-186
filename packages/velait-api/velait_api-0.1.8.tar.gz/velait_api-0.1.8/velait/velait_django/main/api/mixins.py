from rest_framework.exceptions import NotFound
from django.utils.translation import gettext_lazy as _

from velait.common.exceptions import AlreadyDeletedError
from velait.velait_django.main.services.services import delete_object


class SoftDeleteViewMixin:
    def perform_destroy(self, instance):
        try:
            delete_object(instance)
        except AlreadyDeletedError:
            raise NotFound(detail=_("Уже удален"), code="obj")
