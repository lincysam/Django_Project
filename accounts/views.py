from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request):
    return render(request,'register.html')
def index(request):
    return render(request,'index.html')
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'smartphone/mobilecenter.html')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('/accounts/login')
    else:
        return render(request,'login.html')    
def registration(request):
    if request.method == 'POST':
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        email=request.POST['email']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if(password1 == password2):
            if User.objects.filter(username = username).exists():
                messages.info(request,'Username Taken')
                return redirect('/accounts/register')
            elif User.objects.filter(email = email).exists():
                messages.info(request,'Email Taken already')
                return redirect('/accounts/register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=fname,last_name=lname)
                user.save()
                print("user Created")
                return render(request,'login.html')
        else:
            messages.info(request,'Password Not Matching')
            return redirect('/accounts/register')


    