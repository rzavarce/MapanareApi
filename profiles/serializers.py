from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'address', 'avatar', 'birth_date', 'city',
                  'country', 'organization', 'phone_number', 'timezone',
                  'website', 'zip_code', 'nickname', 'age', 'type_user',
                  'activation_token', 'key_expires'
        )