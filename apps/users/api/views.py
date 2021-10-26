from rest_framework import status
from rest_framework.response import Response
from apps.users.api.serializers import RegisterUserSerializer, UserListSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from apps.users.models import User
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


class UserListView(APIView):
    permission_classes = [UserPermissions, ]

    def get(self, request):
        users = User.objects.all().values('id', 'email', 'password', 'name', 'last_name')
        users_serializer = UserListSerializer(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)


class UserDetailView(APIView):
    permission_classes = [UserPermissions, ]

    def get(self, request, pk):
        user = get_object_or_404(User, id=pk)
        self.check_object_permissions(request, user)
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        user = get_object_or_404(User, id=pk)
        self.check_object_permissions(request, user)
        user_serializer = UserSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRegistrationView(APIView):

    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully!'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'There was and error!', 'detail': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)


class UserLogOut(APIView):

    def get(self, request):
        try:
            refresh_token = request.GET["refresh_token"]
            refresh_token = RefreshToken(refresh_token)
            refresh_token.blacklist()
            return Response({'message': 'Token Deleted Succesfully'}, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'There was and error'}, status=status.HTTP_400_BAD_REQUEST)
