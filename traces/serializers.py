from rest_framework import serializers

from .models import Trace


class TraceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trace
        fields = "__all__"
