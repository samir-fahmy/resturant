import os
from django.urls import path,include
from django.contrib.auth import views as auth_views


urlpatterns = [
path('',include('purchases.Supplier.urls')),
]
