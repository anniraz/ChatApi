from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    
    username=models.CharField(max_length=255, unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    age=models.PositiveIntegerField(blank=True,null=True)
    image = models.ImageField(upload_to='profile/',blank=True,null=True)
    last_action=models.DateTimeField(default=timezone.now())
    is_online=models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.username