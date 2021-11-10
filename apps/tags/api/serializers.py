from rest_framework import serializers
from apps.tags.models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'is_active': instance.is_active,
            'products': instance.products.all().values('id', 'name')
        }