import os
from django.urls import path
from .views import unit_item,UnitJson

#from .views import UserDataJson,RegisterView
urlpatterns=[
    path('unit/', unit_item.as_view(), name='unit'),
    path('unitJson/', UnitJson.as_view(), name='UnitJson'),]