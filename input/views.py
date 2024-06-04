from django.views.generic.edit import CreateView
from django.shortcuts import render,redirect

from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import views as auth_views #new
from django.shortcuts import get_object_or_404

from django.http import HttpResponse,JsonResponse 
from django.views import View
#from .forms import RegisterForm
from pyexpat.errors import messages
from django.urls import reverse
from django.core import serializers
from django.http import QueryDict
