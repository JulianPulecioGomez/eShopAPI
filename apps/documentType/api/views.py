from apps.documentType.models import DocumentType
from apps.documentType.api.serializers import DocumentTypeSerializer
from rest_framework import viewsets


class DocumentTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer
