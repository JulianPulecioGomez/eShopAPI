from rest_framework import serializers
from apps.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def update(self, instance, validated_data):
        updated_product = super().update(instance, validated_data)
        print(updated_product)
        for tag in updated_product.tags.all():
            updated_product.tags.remove(tag)
            tag.products.remove(updated_product)
        for tag in self.validated_data.get('tags'):
            updated_product.tags.add(tag)
            tag.products.add(updated_product)
            tag.save()
        updated_product.save()
        return updated_product

    def save(self):
        product = Product(
            name=self.validated_data.get('name'),
            description=self.validated_data.get('description'),
            price=self.validated_data.get('price'),
            stock=self.validated_data.get('stock'),
        )
        product.save()
        for tag in self.validated_data.get('tags'):
            product.tags.add(tag)
            tag.products.add(product)
        product.save()
        return product


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'price': instance.price,
            'stock': instance.stock,
            'tags': instance.tags.all().values('id', 'name')
        }
