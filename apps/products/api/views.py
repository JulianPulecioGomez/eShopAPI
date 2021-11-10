from apps.products.api.serializers import ProductSerializer
from apps.tags.models import Product
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
