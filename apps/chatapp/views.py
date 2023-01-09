from django.db.models import Q

from rest_framework import generics,permissions
from rest_framework.response import Response

from apps.user.models import User  
from apps.user.serializers import UsersListSerializer                             
from apps.chatapp.models import Message,ChatRoom
from apps.chatapp.serializers import MessageSerializer,ChatRoomSerializer,ContactSenderSerializer,ContactReceiverSerializer
from apps.chatapp.permissions import IsChatOwners,PersonalMessages,IsMessageOwner




class  ChatRoomApiView(generics.CreateAPIView):

    '''for creating chats room'''

    queryset=ChatRoom.objects.all()
    serializer_class=ChatRoomSerializer
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user,name_owner='')



class  ContactApiView(generics.RetrieveUpdateDestroyAPIView):

    '''for rename contact and delete '''

    queryset=ChatRoom.objects.all()
    serializer_class=ChatRoomSerializer
    permission_classes=[IsChatOwners]

    def get_serializer_class(self):
        pk = self.kwargs.get('pk')
        chat_room=ChatRoom.objects.get(id=pk)
        if chat_room.owner == self.request.user:
            return ContactSenderSerializer
        elif chat_room.receiver == self.request.user:
            return ContactReceiverSerializer
        else:
            return ChatRoomSerializer


class LIstOfContacts(generics.ListAPIView):

    '''Your all contacts list '''

    queryset=ChatRoom.objects.all()
    serializer_class=ChatRoomSerializer
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        return ChatRoom.objects.filter(Q(owner=self.request.user)|Q(receiver=self.request.user))


class SendMessageApiView(generics.ListCreateAPIView):

    '''To send and receive private messages'''

    queryset=Message.objects.all()
    serializer_class=MessageSerializer
    permission_classes=[PersonalMessages]

    def get(self,request,pk):
        chat_room=ChatRoom.objects.get(id=pk)
        messages=Message.objects.filter(chat_room=chat_room)
        serializer=MessageSerializer(messages,many=True)
        return Response(serializer.data)
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        return serializer.save(chat_room=ChatRoom.objects.get(id=pk))





class MessageDetailApiView(generics.RetrieveUpdateDestroyAPIView):

    '''To delete and update messages'''

    queryset=Message.objects.all()
    serializer_class=MessageSerializer
    permission_classes=[IsMessageOwner]


class AnotherUsersApiView(generics.ListAPIView):

    '''Users with whom there is no chat'''

    queryset=User.objects.all()
    serializer_class=UsersListSerializer

    def get_queryset(self):
        users_id=[self.request.user.id]
        chat=ChatRoom.objects.filter(Q(owner=self.request.user)|Q(receiver=self.request.user))
        for i in chat:
            users_id.append(i.owner.id|i.receiver.id)
        return User.objects.all().exclude(id__in=users_id)

