from rest_framework import serializers

from .models import Vehicles


class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicles
        fields = "__all__"
        depth = 1


class VehicleHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicles.history.model
        fields = ('id', 'nickname', 'history_id', 'history_type',
                  'history_date', 'history_change_reason', 'history_user')


