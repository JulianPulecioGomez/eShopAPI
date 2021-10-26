from rest_framework import serializers
from apps.tags.models import Tag
from apps.products.models import Product
from django.core import serializers as dj_serializers


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

    def update(self, instance, validated_data):
        updated_tag = super().update(instance, validated_data)
        if updated_tag.products.all():
            for product in updated_tag.products.all():
                updated_tag.products.remove(product)
                product.tags.remove(updated_tag)
            for product in self.validated_data.get('products'):
                updated_tag.products.add(product)
                product.tags.add(updated_tag)
            updated_tag.save()
        return updated_tag

    def save(self):
        tag = Tag(name=self.validated_data.get('name'))
        tag.save()
        for product in self.validated_data.get('products'):
            tag.products.add(product)
            product.tags.add(tag)
            product.save()
        tag.save()
        return tag


class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag

    def to_representation(self, instance):
        print(instance.products)
        return {
            'id': instance.id,
            'name': instance.name,
            'products': instance.products.all().values('id', 'name')
        }
