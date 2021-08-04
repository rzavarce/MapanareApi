from rest_framework import serializers
from .models import Client


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'user', 'commercial_name', 'cif', 'commercial_email',
                  'phone_number', 'address', 'zip_code', 'country',
                  'city', 'avatar', 'website', 'description', 'status',
        )