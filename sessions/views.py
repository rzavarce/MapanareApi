from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .serializers import SessionSerializer


class SessionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    # print("pasoooooooooooooooooo")

    # queryset = User.objects.filter(is_active=True)
    # queryset = User.objects.filter(id=1)
    serializer_class = SessionSerializer
    paginator = None

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(id=user.id)

