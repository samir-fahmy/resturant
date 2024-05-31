from django.urls import path
from .views import home, profile, RegisterView

urlpatterns = [
    path('',home,name='index'),
   # path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
]
