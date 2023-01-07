from django.db import models

from apps.user.models import User


class ChatRoom(models.Model):
      name_reciever=models.CharField(max_length=255,null=True,blank=True)
      name_owner=models.CharField(max_length=255,null=True,blank=True)
      receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
      owner= models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')        

      def __str__(self) -> str:
           return f'reciever:{self.name_reciever} sender:{self.name_owner}'
      
      class Meta:
            unique_together=(('receiver','owner',),)


class Message(models.Model):
     chat_room=models.ForeignKey(ChatRoom,on_delete=models.CASCADE)
     message = models.CharField(max_length=1200)
     timestamp = models.DateTimeField(auto_now_add=True)

     def __str__(self):
           return f'message:{self.message}'

     class Meta:
           ordering = ('timestamp',)