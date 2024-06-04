import os
from django.urls import path,include
#from .views import UserDataJson,RegisterView
urlpatterns=[   
    path('',include('input.Category.urls')),
    path('',include('input.Items.urls')),]