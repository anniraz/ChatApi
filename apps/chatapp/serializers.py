from rest_framework import serializers
from apps.chatapp.models import Message,ChatRoom


class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ['id','receiver','name_owner','name_reciever',]
        read_only_fields = ('owner','name_owner',)

    def create(self, validated_data):
        
        if not validated_data['name_reciever'] and not validated_data['name_owner'] :
            validated_data['name_reciever']=validated_data['receiver']
            validated_data['name_owner']=validated_data['owner']
        return super().create(validated_data)


class ContactSenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ['id','receiver','name_reciever','name_owner']
        read_only_fields = ('owner','name_owner')

class ContactReceiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ['id','receiver','name_reciever','name_owner']
        read_only_fields = ('owner','name_reciever',)


class MessageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Message
        fields = ['id','chat_room', 'message', 'timestamp','is_read']
        read_only_fields = ('id','is_read','timestamp','chat_room',)
