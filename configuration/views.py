from django.views.generic.edit import CreateView
from django.shortcuts import render,redirect

from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape
from .forms import UserForm
from django.contrib.auth.models import User
from django.http import HttpResponse,JsonResponse 
from django.views import View
from .forms import RegisterForm
from pyexpat.errors import messages
# Create your views here.

# # class get_users(CreateView): 
# #     def get(self,request,*args,**kwargs):
# #         user=User.objects.all()
# #         fileduse=UserForm()
# #         context={
# #           'user':user,
# #           'filed':fileduse,
# #          } 
# #         return render(request,'configuration/users.html',context) 
# #     def post(self,request,*args,**kwargs):
# #         if not request.POST.get("username"):
# #             context={
# #              "status":0,
# #              "message":"لا يوجد إسم مستخدم"   
# #             }
# #             return JsonResponse(context)
# #     def post(self,request,*args,**kwargs):
# #         if not request.POST.get("password1") or not request.POST.get("password2"):
# #             context={
# #              "status":0,
# #              "message":"يجب عليك كتابة كلمة المرور"   
# #             }
# #             return JsonResponse(context)
# #         print("first_name"*10)
# #         if request.method=='POST':
# #             obje=User.objects.create(
# #                 first_name=request.POST.get('first_name'),
# #                 last_name=request.POST.get('last_name'),                
# #                 username=request.POST.get('username'),            
# #                 password=request.POST.get('password1'),
# #             )
# #             if obje.id:
# #                 context={
# #                     "status":1,
# #                     "message":"تم الحفظ"
# #                 }
# #             else:
# #                 context={
# #                     "status":0,
# #                     "message":"خطأ فى الحفظ"
# #                 }

# #             return JsonResponse(context)

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'configuration/users.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        # if request.user.is_authenticated:
        #     return redirect(to='login')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            # username = form.cleaned_data.get('username')
            # messages.success(request, f'Account created for {username}')
            context={
               "status":1,
               "message":"تم الحفظ",
            }
        else:
            context={
               "status":0,
               "message":"خطأ فى الحفظ",
              #  "message":form.errors,
            }    
        return JsonResponse(context)

        # return render(request, self.template_name, {'form': form})


# def get_users(request):
#     user=User.objects.all()
#     fileduse=UserForm()
#     context={
#         "user":user,
#         "filed":fileduse,
#     }
#     return render(request,'configuration/users.html',context)

class UserDataJson(BaseDatatableView):
  # The model we're going to show
    model = User
   # define the columns that will be returned
    columns = [
        'id',
        'first_name',
        'last_name',
        'username',                     
          ]
    # define column names that will be used in sorting
    # order is important and should be same as order of columns
    # displayed by datatables. For non-sortable columns use empty
    # value like ''
    order_columns = [
        'id',
        'first_name',                     
        'last_name',
        'username', 
          ]

    # set max limit of records returned, this is used to protect our site if someone tries to attack our site
    # and make it return huge amount of data
    max_display_length = 500

    def render_column(self, row, column):
        # We want to render user as a custom column
         return super(UserDataJson, self).render_column(row, column)

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
