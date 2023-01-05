from django.urls import path
from .views import *


urlpatterns = [
    path('messages/<int:pk>/',SendMessageApiView.as_view()),
    path('messages/detail/<int:pk>/',MessagesApiView.as_view()),

]
