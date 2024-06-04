import os
from django.urls import path
from .views import Items_item,ItemsJson

#from .views import UserDataJson,RegisterView
urlpatterns=[
    path('Items/',Items_item.as_view(), name='Items'),
    path('ItemsJson/', ItemsJson.as_view(), name='ItemsJson'),]