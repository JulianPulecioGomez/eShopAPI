from rest_framework import serializers
from apps.users.models import User

class RegisterUserSerializer(serializers.ModelSerializer):
    
    confirm_password = serializers.CharField(
        style={'input_style':'password'},
        write_only=True
    )

    class Meta:
        model = User
        fields = [ 'email', 'name', 'last_name', 'password', 'confirm_password']
        extra_fields = {
            'password': {'write_only':True}
        }
    
    def save(self):
        user = User(
            email = self.validated_data.get('email'),
            name = self.validated_data.get('name'),
            last_name = self.validated_data.get('last_name')
        )

        password = self.validated_data.get('password')
        confirm_password = self.validated_data.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError({'password': 'Passwords must match'})
        user.set_password(password)
        user.save()
        return user