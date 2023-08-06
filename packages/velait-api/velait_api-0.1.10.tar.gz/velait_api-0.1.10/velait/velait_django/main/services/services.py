from uuid import UUID

from django.db.models import QuerySet
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from velait.common.exceptions import AlreadyDeletedError
from velait.velait_django.main.models import BaseModel
from velait.velait_django.main.services.decorators import (
    only_decorator,
    get_related_decorator,
    ordering_decorator,
    pagination_decorator,
    first_object_decorator,
)


User = get_user_model()


def get_object(objects, *args, **kwargs):
    return filter_objects(objects, *args, **kwargs, first=True)


@first_object_decorator
@only_decorator
@pagination_decorator
@ordering_decorator
@get_related_decorator
def filter_objects(objects, *args, **kwargs) -> QuerySet:
    return objects.filter(*args, **kwargs)


@first_object_decorator
@only_decorator
@pagination_decorator
@ordering_decorator
@get_related_decorator
def all_objects(objects):
    return filter_objects(objects)


def empty_objects(objects) -> QuerySet:
    return objects.none()


def object_exists(objects, **kwargs) -> bool:
    return filter_objects(objects, **kwargs).exists()


def delete_object(model: BaseModel):
    if model.is_deleted:
        raise AlreadyDeletedError(name="obj", description=_("Уже удалено"))

    model.is_deleted = True
    model.save(update_fields=['is_deleted'])


def update_object(model: BaseModel, updated_by_id: UUID, **kwargs):
    for key, value in kwargs.items():
        setattr(model, key, value)

    model.updated_by_id = updated_by_id
    model.save(update_fields=('updated_by_id', *kwargs.keys()))


__all__ = [
    'get_object',
    'filter_objects',
    'all_objects',
    'empty_objects',
    'object_exists',
    'update_object',
    'delete_object',
]
