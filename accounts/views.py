from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Create your views here.
def register(request):
    if request.method == 'POST':
      
        username=request.POST["username"]
        email=request.POST["email"]
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
       
        
       
        user=User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name)
        user.save()
        print("done")
    else:
        return render(request,'accounts/register.html')
def login(request):
    return render(request,'accounts/login.html')
def dashboard(request):
    return render(request,'accounts/dashboard.html')