from django.shortcuts import render
import datetime,time
from .models import *
from datetime import *

# Create your views here.
def homepage(request):
    return render(request,'mobilecenter.html')

def brandpage(request):
    return render(request,'brand.html')
    
def createbrand(request):
    if request.method =='POST':
        print("Hellooooooo")
        brandname=request.POST['brandname']
        brandfile=request.FILES['myfile']
        now = datetime.now()
        print("Brandname:  ",brandname)
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
        
        modelobj=phonemodel.objects.filter(id=model_id)
        return render(request,'trans.html',{'modelobj': modelobj})
def payment(request):
        msg="You have compleated your transaction successfully"
        return render(request,'success.html',{'msg':msg})