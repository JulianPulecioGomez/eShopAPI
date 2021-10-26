from rest_framework import status
from rest_framework.response import Response
from apps.products.api.serializers import ProductSerializer, ProductListSerializer
from apps.tags.models import Product
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


class UserPermissions(BasePermission):
    message = 'Editing Users is retricted for your role'

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return request.user == obj

    def has_permission(self, request, obj):
        return request.user and request.user.is_authenticated


class ProductListView(APIView):

    def get(self, request):
        products = Product.objects.all()
        tag_serializer = ProductListSerializer(products, many=True)
        return Response(tag_serializer.data, status=status.HTTP_200_OK)


class ProductDetailView(APIView):
    # permission_classes = [UserPermissions, ]

    def get(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        self.check_object_permissions(request, product)
        product_serializer = ProductListSerializer(product)
        return Response(product_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        self.check_object_permissions(request, product)
        product_serializer = ProductSerializer(product, data=request.data)
        if product_serializer.is_valid():
            product_serializer.update(product, request.data)
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        self.check_object_permissions(request, product)
        product.delete()
        return Response({'message': 'Product deleted successfully!'}, status=status.HTTP_200_OK)


class ProductCreateView(APIView):
    # permission_classes = [UserPermissions, ]

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Product created successfully!'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'There was and error!', 'detail': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
