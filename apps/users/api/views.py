from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from apps.users.api.serializers import RegisterUserSerializer

@api_view(['POST',])
def registration_view(request):
    serializer = RegisterUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({'message':'User created seccesfully!'},status = status.HTTP_201_CREATED)
    else:
        data = serializer.errors
        return Response(user_serializer.errors,status = status.HTTP_400_BAD_REQUEST)

