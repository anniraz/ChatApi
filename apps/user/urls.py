from django.urls import path

from .views import *

urlpatterns = [
    path('',UserListCreateApiView.as_view()),
    path('detail/<int:pk>/',UserDetailApiView.as_view()),
    path('me/',CurrentUserApiView.as_view(),kwargs={'pk': 'me'})
]