from rest_framework import serializers
from apps.documenttype.models import Documenttype

class DocumenttypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documenttype

    def to_representation(self,instance):
        return {
            'id': instance.id,
            'name': instance.name,
        }