from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    company=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    e_mail=models.EmailField(max_length=200)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    contact_no=models.CharField(max_length=12)
    contact_no2=models.CharField(max_length=12)
    address=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    district=models.CharField(max_length=200)
    d_o_b=models.DateField(max_length=200)
    joining_date=models.DateField(max_length=200)
    p_code=models.CharField(max_length=6)
    Image=models.ImageField(upload_to='photos/%Y/%m/%d/')
    about=models.TextField(blank=True)
    def __str__(self):
        return self.username
    list_filter =('user')



 