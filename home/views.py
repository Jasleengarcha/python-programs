from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.

def index(request):
    dict={}
    if(request.method =='POST'):
        first_name= request.POST.get('fname')
        last_name = request.POST.get('lname')

        dict={'first_name':first_name,
                'last_name':last_name}
        
    return render(request, 'index.html',context=dict)

def home(request):
        return HttpResponse("Hello Home")

def about(request):
    dict1 = {}
    if(request.method == 'POST'):
        username = request.POST.get('username')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        male = request.POST.get('male')
        female = request.POST.get('female')
        DOB = request.POST.get('birthday')
        password = request.POST.get('password')
        
        user_details = UserDetails(
            user_name = username,
            user_email = email,
            user_contact = mobile,
            user_gender = "M or F",
            user_dob = DOB,
            user_pswd = password,  
        )
        user_details.save()
        
        dict1 = {'username' : username,
                    'email' : email,
                    'mobile' : mobile,
                    'male' : male,
                    'female' : female,
                    'DOB' : DOB,
                    'password' : password }

    return render(request, 'about-us.html', context=dict1) 
