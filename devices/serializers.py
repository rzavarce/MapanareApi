from rest_framework import serializers
from .models import Device


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('id', 'device_imei', 'sim_phone', 'password', 'type_device',
                  'model_device', 'firmware_device', 'status', 'description'
        )