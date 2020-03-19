from django.shortcuts import render,redirect
from django.http import HttpResponse
from users.models import User
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'users/users.html')
def login_user(request):
    
    if request.method == 'POST':
        
        username =request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username, password=password).exists():
            objects = User.objects.filter(username=username)
            for obj in objects:
                context={
                    'obj':obj
                }
            messages.error(request,'Testing error')
            return render(request,'users/user_dashboard.html',context,{ 'mapbox_access_token': mapbox_access_token })
        else:
            messages.error(request,'Testing error')
            return redirect ('login_user')
    else:
        return render(request,'users/login.html')
def add_register(request):
    
        company=request.POST["company"]
        username=request.POST["username"]
        password=request.POST["password"]
        e_mail=request.POST["e_mail"]
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        contact_no=request.POST["contact_no"]
        contact_no2=request.POST["contact_no2"]
        address=request.POST["address"]
        country=request.POST["country"]
        state=request.POST["state"]
        district=request.POST["district"]
        d_o_b=request.POST["d_o_b"]
        joining_date=request.POST["joining_date"]
        p_code=request.POST["p_code"]
        Image=request.POST["Image"]
        about=request.POST["about"]

        add_user=User(company=company,username=username,password=password,e_mail=e_mail,first_name=first_name,last_name=last_name,contact_no=contact_no,contact_no2=contact_no2,address=address,country=country,state=state,district=district,d_o_b=d_o_b,joining_date=joining_date,p_code=p_code,Image=Image,about=about)
        print("done")
        add_user.save()
        return HttpResponse("Inserted SuccessFuly..")
        
        return HttpResponse("Inserted UNSuccessFuly..")
def change_password(request):
   
    if request.method == 'POST':
        username =request.POST['username']
        password = request.POST['password']
        
        # if User.objects.filter(username=username).exists():
            
        #     User.objects.update(password=password)
            
        #     return HttpResponse("Inserted SuccessFuly..")
        # else:
        #     return HttpResponse("Inserted UNSuccessFuly..")
        objects = User.objects.filter(username=username)
        for obj in objects:
            obj.password = request.POST['password']
            obj.save()
            return HttpResponse("Inserted SuccessFuly..")
    else:
        return render(request,'users/change_password.html')
mapbox_access_token = 'pk.eyJ1IjoiYmlwbGFiOTUiLCJhIjoiY2szdHR0d3RuMDY1eTNtcGszeHRodWVvdSJ9.QB3p-UPze4_dViX59q94_Q'
def user_dashboard(request):
    return render(request,'users/user_dashboard.html', { 'mapbox_access_token': mapbox_access_token })