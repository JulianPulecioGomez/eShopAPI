from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'last_name', 'phone']

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'email': instance.email,
            'name': instance.name,
            'last_name': instance.last_name,
            'phone': instance.phone,
            'document_type': instance.document_type.id,
            'document': instance.document,
        }


class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        style={'input_style': 'password'},
        write_only=True,
        required=False
    )
    password = serializers.CharField(
        style={'input_style': 'password'},
        write_only=True,
        required=False
    )

    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'last_name', 'phone', 'document_type', 'document', 'password',
                  'confirm_password']

    def create(self, validated_data):
        self.check_password()
        user = User.objects.create(
            email=validated_data.get('email'),
            name=validated_data.get('name'),
            last_name=validated_data.get('last_name'),
            phone=validated_data.get('phone'),
            document_type=validated_data.get('document_type'),
            document=validated_data.get('document'),
        )
        user.set_password(validated_data.get('password'))
        user.save()
        return user

    def check_password(self):
        password = self.validated_data.get('password')
        confirm_password = self.validated_data.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError({'password': 'Passwords must match'})
        return True
