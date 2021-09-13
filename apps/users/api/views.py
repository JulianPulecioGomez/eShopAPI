from rest_framework import status
from rest_framework.response import Response
from apps.users.api.serializers import RegisterUserSerializer, UserListSerializer, UserSerializer
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from apps.users.models import User
from rest_framework.permissions import IsAuthenticated, BasePermission
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from braces.views import GroupRequiredMixin
from rest_framework.views import APIView
from braces.views import GroupRequiredMixin

class UserPermissions(BasePermission):
    message = 'Editing Users is retricted for your role'

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return request.user == obj

    def has_permission(self, request, obj):
        return request.user and request.user.is_authenticated


class user_list_view(APIView):
    permission_classes = [UserPermissions,]

    def get(request):
        users = User.objects.all().values('id','email','password','name','last_name')
        users_serializer = UserListSerializer(users,many = True)
        return Response(users_serializer.data,status = status.HTTP_200_OK)

class user_detail_view(APIView):
    permission_classes = [UserPermissions,]
    

    def get(self,request,pk):
        user = User.objects.filter(id = pk).first()
        self.check_object_permissions(request, user)    
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data,status = status.HTTP_200_OK)
    
    def put(self,request,pk):
        user = User.objects.filter(id = pk).first()
        self.check_object_permissions(request, contact)
        user_serializer = UserSerializer(user,data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data,status = status.HTTP_200_OK)
        return Response(user_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        user = User.objects.filter(id = pk).first()
        self.check_object_permissions(request, contact)
        user.delete()
        return Response({'message':'User deleted successfully!'},status = status.HTTP_200_OK)
    

class registration_view(APIView):

    def post(request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message':'User created seccesfully!'},status = status.HTTP_201_CREATED)
        else:
            data = serializer.errors
            return Response(user_serializer.errors,status = status.HTTP_400_BAD_REQUEST)

class log_out(APIView):
    
    def get(request):
        refresh_token = request.data["refresh_token"]
        refreshToken = RefreshToken(refresh_token)
        refreshToken.blacklist()

        return Response({'message':'Token Deleted Succesfully'},status = status.HTTP_202_OK)