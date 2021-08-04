from rest_framework import serializers

from .models import Vehicles
from devices.models import Device
from devices.serializers import DeviceSerializer


class VehicleSerializer(serializers.ModelSerializer):

    # device = serializers.StringRelatedField(many=True)

    devices_list = serializers.SerializerMethodField()

    def get_devices_list(self, obj):
        query = Device.objects.all()
        serie = DeviceSerializer(query, many=True).data
        print()
        print(serie)
        print()
        return serie

    class Meta:
        model = Vehicles
        # fields = "__all__"
        fields = ('id', 'nickname', 'type', 'category', 'model',
                  'serie', 'registration_number', 'manufacturing_year',
                  'manufacturer', 'engine_type', 'engine_model', 'fuel_type',
                  'fuel_capacity', 'number_seats', 'description', 'status',
                  'status_dry', 'device', 'client', 'devices_list')
        depth = 1
