from django.views.generic.edit import CreateView
from django.shortcuts import render,redirect

from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape
from .forms import UnitForm
from configuration.models import Unit

from django.http import HttpResponse,JsonResponse 
from django.views import View
from .forms import UnitForm
from pyexpat.errors import messages
class unit_item(CreateView): 
    def get(self,request,*args,**kwargs):
        unit=Unit.objects.all()
        fileduse=UnitForm()
        context={
          'Unit':unit,
          'filed':fileduse,
         } 
        return render(request,'configuration/unit/unit_item.html',context) 
    def post(self,request,*args,**kwargs):
        form = UnitForm(request.POST)
        unit=""
        if form.is_valid():
            unit=form.save()
            if unit.id:
                context={
                    "status":1,
                    "message":"تم الحفظ"
                }
            else:
                context={
                    "status":0,
                    "message":"خطأ فى الحفظ"
                }
            return JsonResponse(context)    
class UnitJson(BaseDatatableView):
  # The model we're going to show
    model = Unit
   # define the columns that will be returned
    columns = [
        'id',
        'name_lo',
        'name_fk',
        'codeUnit',                     
          ]
    # define column names that will be used in sorting
    # order is important and should be same as order of columns
    # displayed by datatables. For non-sortable columns use empty
    # value like ''
    order_columns = [
        'id',
        'name_lo',                     
        'name_fk',
        'codeUnit', 
          ]

    # set max limit of records returned, this is used to protect our site if someone tries to attack our site
    # and make it return huge amount of data
    max_display_length = 500

    def render_column(self, row, column):
        # We want to render user as a custom column
         return super(UnitJson, self).render_column(row, column)

    def filter_queryset(self, qs):
        # use parameters passed in GET request to filter queryset

        # simple example:
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(name__istartswith=search)

        # more advanced example using extra parameters
        filter_customer = self.request.GET.get('customer', None)

        if filter_customer:
            customer_parts = filter_customer.split(' ')
            qs_params = None
            for part in customer_parts:
                q = Q(customer_firstname__istartswith=part) | Q(customer_lastname__istartswith=part)
                qs_params = qs_params | q if qs_params else q
            qs = qs.filter(qs_params)
        return qs
