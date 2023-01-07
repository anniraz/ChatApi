from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from utils.NumberValidator import phone_validator


class User(AbstractUser):
    
    username=models.CharField(max_length=255, unique=True)
    email=models.EmailField(blank=True,null=True)
    phone_number = models.CharField(max_length=13,validators=[phone_validator],blank=True,null=True)
    age=models.PositiveIntegerField(blank=True,null=True)
    bio=models.CharField(max_length=400,blank=True,null=True)
    image = models.ImageField(upload_to='profile/',blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    last_action=models.DateTimeField(default=timezone.now())
    is_online=models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.username
        