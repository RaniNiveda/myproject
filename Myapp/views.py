
#author raniniveda
from rest_framework import viewsets

from . import models
from . import Serializer

class UserListView(viewsets.ModelViewSet):
    queryset = models.UserProfile.objects.all()
    serializer_class = Serializer.UserSerializer