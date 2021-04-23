from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import TraceSerializer
from .models import Trace


class TraceListCreateAPIView(ListCreateAPIView):
    """
    API view to retrieve list of posts or create new
    """
    serializer_class = TraceSerializer
    queryset = Trace.objects.all().order_by('id')


class TraceDetailsAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete post
    """
    serializer_class = TraceSerializer
    queryset = Trace.objects.all().order_by('id')

