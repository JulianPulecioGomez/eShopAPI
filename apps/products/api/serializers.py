from rest_framework import serializers
from apps.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'price': instance.price,
            'stock': instance.stock,
            'is_active': instance.is_active,
            'tags': instance.tags.all().values('id', 'name')
        }