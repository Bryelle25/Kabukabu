from rest_framework import serializers
from business.models import Business


class BusinessSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    type = serializers.CharField(max_length=255)
    country = serializers.CharField(max_length=255)
    state = serializers.CharField(max_length=255)
    street = serializers.CharField(max_length=255)
    phone = serializers.CharField(max_length=25)
    logo = serializers.ImageField()

    class Meta:
        model = Business
        fields = ['id', 'name', 'type', 'country', 'state', 'street', 'phone', 'logo', 'created_at', 'city']