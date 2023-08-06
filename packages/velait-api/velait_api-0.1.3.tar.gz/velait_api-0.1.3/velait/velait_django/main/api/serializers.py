from rest_framework.serializers import ModelSerializer

from velait.velait_django.main.models import BaseModel


class BaseSerializer(ModelSerializer):
    class Meta:
        model = BaseModel
        fields = (
            "uuid",
            "is_deleted",
            "created_at",
            "created_by_id",
            "updated_at",
            "updated_by_id",
        )
        read_only_fields = (
            "uuid",
            "is_deleted",
            "created_at",
            "created_by_id",
            "updated_at",
            "updated_by_id",
        )
        abstract = True


__all__ = ['BaseSerializer']
