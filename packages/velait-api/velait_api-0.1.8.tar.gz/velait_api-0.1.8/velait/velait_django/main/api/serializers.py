from rest_framework.serializers import ModelSerializer
from rest_framework.utils import model_meta

from velait.velait_django.main.models import BaseModel
from velait.velait_django.main.services.services import update_object


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

    def get_user_uuid(self, instance):
        raise NotImplementedError("You need to add get_user() function to your serializers")

    def update(self, instance, validated_data):
        info = model_meta.get_field_info(instance)

        many_to_many_fields = []
        update_values = {}

        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                many_to_many_fields.append((attr, value))
            else:
                update_values[attr] = value

        update_object(model=instance, updated_by_id=self.get_user_uuid(instance), **update_values)

        for attr, value in many_to_many_fields:
            field = getattr(instance, attr)
            field.set(value)

        return instance

    def create(self, validated_data):
        info = model_meta.get_field_info(self.Meta.model)

        many_to_many = {}

        for field_name, relation_info in info.relations.items():
            if relation_info.to_many and (field_name in validated_data):
                many_to_many[field_name] = validated_data.pop(field_name)

        instance = self.Meta.model.objects.create(**validated_data, created_by_id=self.get_user_uuid(None))

        if many_to_many:
            for field_name, value in many_to_many.items():
                field = getattr(instance, field_name)
                field.set(value)

        return instance


__all__ = ['BaseSerializer']
