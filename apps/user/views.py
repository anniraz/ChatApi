from rest_framework import generics

from apps.user.models import User
from apps.user.serializers import UserSerializer,UsersListSerializer


class UserListCreateApiView(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer


class UserDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer