from rest_framework import generics,permissions

from apps.user.models import User
from apps.user.permissions import IsOwner
from apps.user.serializers import UserSerializer,UsersListSerializer


class UserListCreateApiView(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer


class UserDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[IsOwner]

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes=[permissions.IsAuthenticated]
        else:
            permission_classes=[IsOwner]
        return [permission() for permission in permission_classes]