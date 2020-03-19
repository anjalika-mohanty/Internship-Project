from django.shortcuts import render
from django.http import HttpResponse
from users.models import User
from pages.models import Attendance
from django.utils import timezone
def index(request):
    return render(request,'pages/index.html')

def about(request):
    return render(request,'pages/about.html')
def login(request):
    return render(request,'pages/login.html')
def Add_user(request):
    return render(request,'pages/register_user.html')
def Dash_board(request):
    return render(request,'pages/dashboard.html')
def user_profile(request):
    return render(request,'dashboard/user_profile.html')
def map(request):
    return render(request,'dashboard/map.html')
def add_attendace(request):
    if request.method == 'POST':
        name =request.POST['name']
        In_time=timezone.now()
        currentdate=timezone.now()
        locationn=request.POST['locationn']
        if Attendance.objects.filter(name=name,currentdate=currentdate).exists():
           return HttpResponse("You already check in !!") 
        else:
            add_user=Attendance(name=name,In_time=In_time,currentdate=currentdate,locationn=locationn)
            add_user.save()
            return HttpResponse("Thank You U!!! login again to check out")
def add_checkout(request):
    if request.method == 'POST':
        name =request.POST['name']
        currentdate=timezone.now()
        objects = Attendance.objects.filter(name=name,currentdate=currentdate)
        for obj in objects:
            obj.Out_time = timezone.now()
            obj.save()
            return HttpResponse("Inserted SuccessFuly..")
    else:
        return HttpResponse("Thank You U!!! login again to check out")
    