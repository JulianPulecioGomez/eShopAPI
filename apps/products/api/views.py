from apps.products.api.serializers import ProductSerializer
from apps.tags.models import Product
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, parsers


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    permission_classes = [IsAuthenticated]
