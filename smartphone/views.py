from django.shortcuts import render
import datetime,time
from .models import *
from datetime import *
from django.contrib.auth.models import User
# Create your views here.
def homepage(request):
    return render(request,'mobilecenter.html')

def brandpage(request):
    return render(request,'brand.html')
    
def createbrand(request):
    if request.method =='POST':
        
        brandname=request.POST['brandname']
        brandfile=request.FILES['myfile']
        now = datetime.now()
        
        savedata=brand(brandname=brandname,created_at=now,updated_at=now,brand_image=brandfile)
        savedata.save()
        msg="Data saved"
        return render(request,'mobilecenter.html')
def modelpage(request):
    brandobj=brand.objects.all()
    return render(request,'model.html',{'brandobj':brandobj})   

def  createmodel(request):
    if request.method =='POST':
        brand_id=request.POST['brand_id']
        modelname=request.POST['modelname']
        release_year=request.POST['release_year']
        quantity=request.POST['quantity']
        price=request.POST['price']
        available=request.POST['available']
        mobile_image=request.FILES['myfile']
        now = datetime.now()
        
        bid=brand(id=brand_id)
        savedata=phonemodel(brand_id=bid,created_at=now,updated_at=now,mobile_image=mobile_image,modelname=modelname,release_year=release_year,available_quantities=quantity,price=price,is_available=available)
        savedata.save()
        msg="Data saved"
        return render(request,'mobilecenter.html')
def brandlist(request):
         
        brandobj=brand.objects.all()
        return render(request,'listbrand.html',{'brandobj': brandobj})
def modellist(request):
        brand_id=request.GET['brand_id']
        modelobj=phonemodel.objects.filter(brand_id=brand_id)
        return render(request,'listmodel.html',{'modelobj': modelobj})
def transaction(request):
        model_id=request.GET['model_id']
        
        modelobj=phonemodel.objects.get(id=model_id)
        print("Name:",modelobj)
        return render(request,'trans.html',{'modelobj': modelobj})
def payment(request):
    if request.method=='POST':
        trans_model=request.POST['model_id']
        modelobj=phonemodel.objects.get(id=trans_model)
        userdata = User.objects.get(username=request.user)
        model_id=phonemodel(id=trans_model)
        transaction_type=request.POST['transtype']
        t_amount=modelobj.price
        savedata=mobile_trans(trans_model=model_id,transaction_type=transaction_type,t_amount=t_amount,usersample=userdata)
        savedata.save()
        msg="You have completed your transaction successfully"
        return render(request,'success.html',{'msg':msg})