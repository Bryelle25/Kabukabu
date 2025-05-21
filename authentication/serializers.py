from rest_framework import serializers
from user.models import CustomUser
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from utils.emails import send_email    
class SignUpSerializer(serializers.ModelSerializer):
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    date_of_birth = serializers.DateField()
    gender = serializers.ChoiceField(choices = ['MALE', 'FEMALE'])
    profile_picture = serializers.ImageField(required = False)
    nationality = serializers.CharField()
    address = serializers.CharField(required = False)
    user_type = serializers.ChoiceField(choices = ['CUSTOMER', 'RIDER', 'STAFF', 'ADMIN'])
    
    
    class Meta:
        model = CustomUser
        fields = ('firstname', 'lastname', 'email', 'password',
                  'date_of_birth','address', 'user_type', 'nationality',
                  'profile_picture', 'gender')
        
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ("id","tokens", "email", "password")

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        user = auth.authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed("Invalid Login credentials")
        data = {
            "to": email,
            "subject": "Welcome back to Kabu kabu!",
            "message": (
                "Hi,\n\n"
                "Welcome back to Kabu kabu. We’re thrilled to have you back at Kabukabu where riders thrive!\n"
                "Let’s keep riding.\n\n"
            )
        }
        send_email(data)
        return {
            "id": user.id,
            "email": user.email,
            "tokens": user.tokens,
        }
