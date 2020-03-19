from django.utils import timezone

from django.db import models
class Attendance(models.Model):
    name= models.CharField(max_length=150)  
    In_time = models.DateTimeField()
    Out_time = models.DateTimeField()
    currentdate= models.DateField()
    locationn=models.CharField(max_length=150) 
    def __str__(self):
        return self.name
    list_filter =('name')
