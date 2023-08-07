from django.db import models


class StateType(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class PassType(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class User1(models.Model):
	name = models.CharField(max_length=100 ,verbose_name='نام کاربری')
	personeli = models.CharField(max_length=20,unique=True,verbose_name='شماره پرسنلی')
	etebar = models.CharField(max_length=10 ,verbose_name='تاریخ ااعتبار')
	pic = models.ImageField(upload_to='images/', blank=True, null=True ,verbose_name='تصویر')
	number = models.IntegerField(default = 1 , unique=True ,verbose_name='شماره کارت')
	def __str__(self):
	    return self.name
		
