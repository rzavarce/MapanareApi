from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from devices.models import Device
from vehicles.models import Vehicles
from devices.serializers import DeviceSerializer
from .serializers import VehicleSerializer, VehicleHistorySerializer
from .models import Vehicles, TYPE, CATEGORY, ENGINE_TYPE, FUEL_TYPE, STATUS, \
    STATUS_DRY, ENGINE_NUMBERS


class VehicleList(generics.ListCreateAPIView):
    model = Vehicles
    queryset = Vehicles.objects.all()
    serializer_class = VehicleSerializer


class VehicleDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Vehicles
    queryset = Vehicles.objects.all()
    serializer_class = VehicleSerializer


class VehicleAddFormData(APIView):
    def get(self, request):
        form_data = set_partial_form_data()

        return Response(form_data)


class VehicleEditFormData(APIView):
    def get(self, request, pk):

        print()
        print(pk)
        print()

        form_data = set_partial_form_data()
        vehicule_query = Vehicles.objects.filter(id=pk)
        form_data["vehicle_data"] = VehicleSerializer(vehicule_query,
                                                      many=True).data

        return Response(form_data)


def set_partial_form_data():
    form_data = dict()

    form_data["type_list"] = TYPE
    form_data["category_list"] = CATEGORY
    form_data["engine_list"] = ENGINE_TYPE
    form_data["fuel_types_list"] = FUEL_TYPE
    form_data["status_list"] = STATUS
    form_data["status_dry_list"] = STATUS_DRY
    form_data["engine_number_list"] = ENGINE_NUMBERS

    devices_query = Device.objects.all()
    form_data["devices_list"] = DeviceSerializer(devices_query,
                                                 many=True).data

    vehicules_history_query = Vehicles.history.all()
    form_data["vehicles_history"] = \
        VehicleHistorySerializer(vehicules_history_query, many=True).data

    return form_data





