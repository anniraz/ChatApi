from django.urls import path
from .views import *


urlpatterns = [
    path('new/contact/',ChatRoomApiView.as_view()),
    path('contact/<int:pk>/',ContactApiView.as_view()),
    path('contacts/',LIstOfContacts.as_view()),
    path('send/message/<int:pk>/',SendMessageApiView.as_view()),
    path('message/<int:pk>/',MessageDetailApiView.as_view()),
    path('users-another/',AnotherUsersApiView.as_view()),

    # path('messages/<int:pk>/',SendMessageApiView.as_view()),
    # path('messages/detail/<int:pk>/',MessagesApiView.as_view()),

]
