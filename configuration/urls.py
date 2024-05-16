import os
from django.urls import path
from .views import UserDataJson,RegisterView
urlpatterns=[
    #path('usersview',get_users.as_view(),name='usersview'),
    path('UserDataJson',UserDataJson.as_view(), name='UserDataJson'),
    path('register/', RegisterView.as_view(), name='users-register'),
]