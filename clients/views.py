from django.shortcuts import render

# Create your views here.
from .models import Client
from .serializers import ClientsSerializer
from rest_framework import generics


class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientsSerializer


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientsSerializer
