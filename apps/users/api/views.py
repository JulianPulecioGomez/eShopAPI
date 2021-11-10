from rest_framework import status
from rest_framework.response import Response
from apps.users.api.serializers import UserSerializer, UserRegistrationSerializer
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from apps.users.models import User
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class UserPermissions(BasePermission):
    message = 'Editing Users is retricted for your role'

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return request.user == obj

    def has_permission(self, request, obj):
        return request.user and request.user.is_authenticated


class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all().filter(is_active=True)
    serializer = UserSerializer

    # permission_classes = [UserPermissions]

    def list(self, request):
        serializer = self.serializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer(user)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        user.delete()
        return Response()


class UserRegistrationViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer = UserRegistrationSerializer
    # permission_classes = [UserPermissions]

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'email': openapi.Schema(
                type=openapi.TYPE_STRING,
                description='email'
            ),
            'name': openapi.Schema(
                type=openapi.TYPE_STRING,
                description='name'
            ),
            'last_name': openapi.Schema(
                type=openapi.TYPE_STRING,
                description='last_name'
            ),
            'other_last_name': openapi.Schema(
                type=openapi.TYPE_STRING,
                description='last_name'
            ),
            'phone': openapi.Schema(
                type=openapi.TYPE_NUMBER,
                description='phone'
            ),
            'document_type': openapi.Schema(
                type=openapi.TYPE_NUMBER,
                description='document_type'
            ),
            'document': openapi.Schema(
                type=openapi.TYPE_NUMBER,
                description='document'
            ),
            'password': openapi.Schema(
                type=openapi.TYPE_STRING,
                description='document'
            ),
            'confirm_password': openapi.Schema(
                type=openapi.TYPE_STRING,
                description='document'
            ),

        }
    ))
    def create(self, request):
        serializer = self.serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
