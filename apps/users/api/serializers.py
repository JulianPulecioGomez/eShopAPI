from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
       
    def update(self,instance,validated_data):
        updated_user = super().update(instance,validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

    def to_representation(self,instance):
        return {
            'id': instance['id'],
            'email': instance['email'],
            'name': instance['name'],
            'last_name': instance['last_name'],
        }

class RegisterUserSerializer(serializers.ModelSerializer):
    
    confirm_password = serializers.CharField(
        style={'input_style':'password'},
        write_only=True
    )

    class Meta:
        model = User
        fields = [ 'email', 'name', 'last_name', 'phone', 'document_type', 'document', 'password', 'confirm_password']
        extra_fields = {
            'other_last_name' : '',
            'password': {'write_only':True}
        }
    
    def save(self):
        user = User(
            email = self.validated_data.get('email'),
            name = self.validated_data.get('name'),
            last_name = self.validated_data.get('last_name'),
            phone = self.validated_data.get('phone'),
            document_type = self.validated_data.get('document_type'),
            document = self.validated_data.get('document'),
        )

        password = self.validated_data.get('password')
        confirm_password = self.validated_data.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError({'password': 'Passwords must match'})
        user.set_password(password)
        user.save()
        return user