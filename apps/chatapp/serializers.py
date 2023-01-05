from rest_framework import serializers
from apps.chatapp.models import Message


class MessageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Message
        fields = ['id','sender','receiver', 'message', 'timestamp','is_read']
        read_only_fields = ('sender','receiver','is_read',)