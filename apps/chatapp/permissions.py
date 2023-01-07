from rest_framework import permissions

from apps.chatapp.models import Message,ChatRoom

class IsChatOwners(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(obj.receiver == request.user or obj.owner == request.user)


class PersonalMessages(permissions.BasePermission):

    def has_permission(self, request, view):
        id =view.kwargs.get('pk')
        room=ChatRoom.objects.get(id=id)
        if room.receiver == request.user or room.owner == request.user:
            return True
        else:
            return False


class IsMessageOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        id =view.kwargs.get('pk')
        msg=Message.objects.get(id=id)
        room=ChatRoom.objects.get(id=msg.chat_room.id)
        if room.receiver == request.user or room.owner == request.user:
            return True
        else:
            return False