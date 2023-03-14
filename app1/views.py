from django.shortcuts import render
from .models import CustomerRegister
from .forms import RegisterForm
# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
   if request.method=='POST':
       user_name=request.POST.get('user_name')
       email=request.POST.get('email')
       password=request.POST.get('password')
       data= CustomerRegister(user_name=user_name,email=email,password=password)
       data.save()
   return render(request,'login.html')    


def index2(request):
    return render(request,'index2.html')

def index3(request):
    return render(request,'index3.html')

def index4(request):
    return render(request,'index4.html')

def index5(request):
    return render(request,'index5.html')



