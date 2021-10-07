from rest_framework import status
from rest_framework.response import Response
from apps.documenttype.models import Documenttype
from apps.documenttype.api.serializers import DocumenttypeListSerializer
from rest_framework.views import APIView

class documenttype_list_view(APIView):

    def get(self,request):
        documentsTypes = Documenttype.objects.all()
        docuementType_serializer = DocumenttypeListSerializer(documentsTypes ,many = True)
        return Response(docuementType_serializer.data,status = status.HTTP_200_OK)