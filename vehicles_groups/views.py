from .models import VehiclesGroup
from .serializers import VehiclesGroupSerializer
from rest_framework import generics


class VehiclesGroupList(generics.ListCreateAPIView):
    queryset = VehiclesGroup.objects.all()
    serializer_class = VehiclesGroupSerializer


class VehiclesGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VehiclesGroup.objects.all()
    serializer_class = VehiclesGroupSerializer
