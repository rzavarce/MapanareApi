from rest_framework import serializers

from .models import VehiclesGroup


class VehiclesGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiclesGroup
        fields = "__all__"
