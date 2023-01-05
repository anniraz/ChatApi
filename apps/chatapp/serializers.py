from rest_framework import serializers
from apps.chatapp.models import Message,ChatRoom


class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ['id','receiver','name']
        read_only_fields = ('owner',)

    def create(self, validated_data):
        
        if not validated_data['name'] :
            validated_data['name']=validated_data['receiver']
        return super().create(validated_data)



class MessageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Message
        fields = ['id','chat_room', 'message', 'timestamp','is_read']
        read_only_fields = ('is_read',)
