from django.db import models

   
class Unit(models.Model):    
   name_lo=models.CharField('الإسم المحلى', max_length=50) 
   name_fk=models.CharField('الإسم الأجنبى', max_length=50) 
   codeUnit=models.CharField('رمز الوحده', max_length=50)
   def __str__(self):
      return self.name_lo
    
class Items_type(models.Model):
   name_lo=models.CharField('الإسم المحلى', max_length=50) 
   name_fk=models.CharField('الإسم الأجنبى', max_length=50) 
   def __str__(self):
      return self.name_lo


class Store(models.Model):
   name_lo=models.CharField('الإسم المحلى', max_length=50) 
   name_fk=models.CharField('الإسم الأجنبى', max_length=50) 
   is_stop=models.BooleanField(default=True)

class Items(models.Model):
   unit=models.ForeignKey(Unit,on_delete = models.CASCADE) 
   items_type=models.ForeignKey(Items_type, on_delete=models.CASCADE)
   barcode=models.CharField('باركود',max_length=50)
   name_lo=models.CharField('اسم الصنف المحلى', max_length=50,unique=True,default=" ") 
   name_fk=models.CharField('اسم الصنف الأجنبى', max_length=50,default=" ") 
 

class story_items(models.Model):
   qty=models.IntegerField('الكمية')    
   items=models.ForeignKey(Items, on_delete=models.CASCADE)
   stor=models.ForeignKey(Store, on_delete=models.CASCADE)
   date_in=models.DateTimeField('تاريخ الإضافه')