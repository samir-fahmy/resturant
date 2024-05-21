import os
from django.urls import path
from .views import Item_type,Item_typeJson

#from .views import UserDataJson,RegisterView
urlpatterns=[
    path('itemstype/', Item_type.as_view(), name='itemstype'),
    path('itemstypeJson/', Item_typeJson.as_view(), name='itemstypeJson'),]