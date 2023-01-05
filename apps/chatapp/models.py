from django.db import models

from apps.user.models import User


class ChatRoom(models.Model):
      receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
      name=models.CharField(max_length=255,null=True,blank=True)
      owner= models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')        

      def __str__(self) -> str:
           return f'{self.name}'

class Message(models.Model):
     chat_room=models.ForeignKey(ChatRoom,on_delete=models.CASCADE)
     message = models.CharField(max_length=1200)
     timestamp = models.DateTimeField(auto_now_add=True)
     is_read = models.BooleanField(default=False)

     def __str__(self):
           return f'message:{self.message}'

     class Meta:
           ordering = ('timestamp',)