import os
from django.urls import path,include
from .views import UserDataJson,RegisterView
urlpatterns=[
    #path('usersview',get_users.as_view(),name='usersview'),
    path('UserDataJson',UserDataJson.as_view(), name='UserDataJson'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('',include('configuration.Unit.urls')),
    path('',include('configuration.itemtype.urls')),
    path('',include('configuration.store.urls')),]