import os
from django.urls import path
from .views import store,StoreJson

#from .views import UserDataJson,RegisterView
urlpatterns=[
    path('store/', store.as_view(), name='store'),
    path('storeJson/', StoreJson.as_view(), name='storeJson'),]