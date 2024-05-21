from django.views.generic.edit import CreateView
from django.shortcuts import render,redirect

from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape
from .forms import StoreForm
from configuration.models import Store

from django.http import HttpResponse,JsonResponse 
from django.views import View
from .forms import StoreForm
from pyexpat.errors import messages
class store(CreateView): 
    def get(self,request,*args,**kwargs):
        store=Store.objects.all()
        fileduse=StoreForm()
        context={
          'store':store,
          'filed':fileduse,
         } 
        return render(request,'configuration/store/store.html',context) 
    def post(self,request,*args,**kwargs):
        form = StoreForm(request.POST)
        store=""
        if form.is_valid():
            store=form.save()
            if store.id:
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
class StoreJson(BaseDatatableView):
  # The model we're going to show
    model = Store
   # define the columns that will be returned
    columns = [
        'id',
        'name_lo',
        'name_fk',
        'is_stop',                     
          ]
    # define column names that will be used in sorting
    # order is important and should be same as order of columns
    # displayed by datatables. For non-sortable columns use empty
    # value like ''
    order_columns = [
        'id',
        'name_lo',                     
        'name_fk',
        'is_stop', 
          ]

    # set max limit of records returned, this is used to protect our site if someone tries to attack our site
    # and make it return huge amount of data
    max_display_length = 500
    count = 0
    def render_column(self, row, column):
        if column =="is_stop":
            if row.is_stop:
              return "مفعل"
            else:
              return "موقف "
        
        if column == "id":
            self.count += 1
            return self.count
        else:
            return super(StoreJson,self).render_column(row, column)


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
