# -*- encoding: utf-8 -*-
from django.urls import path

from .viewsets import TraceDetailsAPIView, TraceListCreateAPIView

urlpatterns = [
    path('traces/', TraceListCreateAPIView.as_view(), name='api-traces-list'),
    path('traces/<uuid:pk>/', TraceDetailsAPIView.as_view(), name='api-traces-details'),
]
