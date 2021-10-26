from rest_framework import status
from rest_framework.response import Response
from apps.tags.api.serializers import TagListSerializer, TagSerializer
from apps.tags.models import Tag
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


class TagListView(APIView):
    permission_classes = [UserPermissions, ]

    def get(self, request):
        tags = Tag.objects.all()
        tag_serializer = TagListSerializer(tags, many=True)
        return Response(tag_serializer.data, status=status.HTTP_200_OK)


class TagDetailView(APIView):
    # permission_classes = [UserPermissions, ]

    def get(self, request, pk):
        tag = get_object_or_404(Tag, id=pk)
        self.check_object_permissions(request, tag)
        tag_serializer = TagSerializer(tag)
        return Response(tag_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        tag = get_object_or_404(Tag, id=pk)
        self.check_object_permissions(request, tag)
        tag_serializer = TagSerializer(tag, data=request.data)
        if tag_serializer.is_valid():
            tag_serializer.update(tag, request.data)
            return Response(tag_serializer.data, status=status.HTTP_200_OK)
        return Response(tag_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        tag = get_object_or_404(Tag, id=pk)
        self.check_object_permissions(request, tag)
        tag.delete()
        return Response({'message': 'Tag deleted successfully!'}, status=status.HTTP_200_OK)


class TagCreateView(APIView):
    # permission_classes = [UserPermissions, ]

    def post(self, request):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created seccesfully!'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'There was and errror!', 'detail': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
