import os
from django.urls import path,include
#from .views import UserDataJson,RegisterView
from .views import Supplier_view,SupplierJson
urlpatterns=[   
    path('Supplier',Supplier_view.as_view(),name='supplier'),
    path('SupplierJson',SupplierJson.as_view(),name='SupplierJson')]