from django.db import models

# Create your models here.
class Supplier(models.Model):
    name_lo=models.CharField('الإسم المحلى', max_length=50)
    name_fk=models.CharField('رقم الجوال', max_length=50,blank=True, null=True)
    phone=models.CharField('الإسم الأجنبى', max_length=50)
    is_stop=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name_lo
    
