from rest_framework import generics,permissions

from apps.user.models import User
from apps.user.permissions import IsOwner
from apps.user.serializers import UserSerializer


class UserListCreateApiView(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[permissions.AllowAny]


class UserDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    '''User's detail'''
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[IsOwner]

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes=[permissions.IsAuthenticated]
        else:
            permission_classes=[IsOwner]
        return [permission() for permission in permission_classes]



class CurrentUserApiView(generics.RetrieveUpdateDestroyAPIView):

    '''current user '''

    queryset=User.objects.all()
    serializer_class=UserSerializer
    # permission_classes=[IsOwner]

    def get_object(self):
        if self.kwargs.get('pk', None) == 'me':
            self.kwargs['pk'] = self.request.user.pk
        return super(CurrentUserApiView, self).get_object()
    
    