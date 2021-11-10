from rest_framework import viewsets
from apps.tags.api.serializers import TagSerializer
from apps.tags.models import Tag
from rest_framework.permissions import IsAuthenticated


class TagViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Tag.objects.all().filter(is_active=True)
    serializer_class = TagSerializer

