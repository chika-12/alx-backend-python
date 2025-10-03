from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework import serializers

class CustomTokenPairSerializer(TokenObtainPairSerializer):

  username_field = 'email'
  def validate(self, attrs):

    email = attrs.get('email')
    password = attrs.get('password')

    if email and password:
      user = authenticate(request=self.context.get('request'), email=email, password=password)
    else:
      raise serializers.ValidationError("Invalid Email or Password")
    
    if not user:
      raise serializers.ValidationError("Invalid Email or Password")
    
    data = super().validate(attrs)
    data['user']={
      'id': str(self.user.user_id),
      'full_name': str(self.user.first_name) + " " + str(self.user.last_name),
      'email': self.user.email,
      'role': self.user.role
    }
    return data