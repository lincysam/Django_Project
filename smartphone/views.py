from django.shortcuts import render
import datetime,time
from .models import *
from datetime import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db.models import Q
from django.db.models import Avg,Sum,Count,Max
# Create your views here.
def homepage(request):
    return render(request,'mobilecenter.html')

def brandpage(request):
    return render(request,'brand.html')
    
def createbrand(request):
    if request.method =='POST':
        try:   
            brandname=request.POST['brandname']
            brandfile=request.FILES['myfile']
            now = datetime.now()
            if(brandname =="" or brandfile==""):
                
                msg="Please fill required fields"
                return render(request,'brand.html',{'msg':msg})
            else:
                savedata=brand(brandname=brandname,created_at=now,updated_at=now,brand_image=brandfile)
                savedata.save()
                msg="Data saved"
                return render(request,'mobilecenter.html')
        except Exception as e:
            print("Some error occured")       
                 
                 
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
        if (int(price) < 0):
            raise ValueError("Work with positive numbers only")
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
        
        
        return render(request,'trans.html',{'modelobj': modelobj})
        
            
def payment(request):
    if request.method=='POST':
        try:
            trans_model=request.POST['model_id']
            
            modelobj=phonemodel.objects.get(id=trans_model)
            
            userdata = User.objects.get(username=request.user)
            model_id=phonemodel(id=trans_model)
            transaction_type=request.POST['transtype']
            t_amount=modelobj.price
            savedata=mobile_trans(trans_model=model_id,transaction_type=transaction_type,t_amount=t_amount,usersample=userdata)
            savedata.save()
            modelobj.available_quantities -=1
            modelobj.updated_at=datetime.now()
            modelobj.save()
            msg="You have completed your transaction successfully"
            return render(request,'success.html',{'msg':msg})
        except Exception as e:
            print("Some Error occured")
def statistics(request):
    maxmodeldict={}
    total_phone=mobile_trans.objects.count()
      
    topselling_model=mobile_trans.objects.values('trans_model').annotate(Count('trans_model'))
    maxmodelcount=0
    countval=len(topselling_model)
    print("Top selling",topselling_model)
    
    for i in range(0,countval):
        if(maxmodelcount < topselling_model[i]['trans_model__count']):
            maxmodelcount = topselling_model[i]['trans_model__count']
            maxmodeldict[topselling_model[i]['trans_model']]=topselling_model[i]['trans_model__count']
        elif(maxmodelcount == topselling_model[i]['trans_model__count']):   
            maxmodeldict[topselling_model[i]['trans_model']]=topselling_model[i]['trans_model__count']

    max_models = [key for key, value in maxmodeldict.items() if value == max(maxmodeldict.values())] 
    # print("Top selling models are:")
    if(len(max_models) > 1):
        
        modelobj=(phonemodel.objects.filter(id__in=max_models))
        modelobj_count=modelobj.count()
        print("Tp_selling_model_count",modelobj_count)
    else:   
        modelobj = phonemodel.objects.get(id = max_models[0])
        modelobj_count = 1
    print("Top selling model",modelobj)
    print("Top selling model count",modelobj_count)
    
    
    modelval=mobile_trans.objects.all()
    branddict={}
    for eachmodel in modelval:
       
        brandobj=brand.objects.get(id=eachmodel.trans_model.brand_id_id)
        if(brandobj.brandname in branddict):
            branddict[brandobj.brandname] += 1
        else:
            branddict[brandobj.brandname] = 1
    max_brand = [key for key, value in branddict.items() if value == max(branddict.values())] 

    
    top_brand=brand.objects.get(brandname=max_brand[0])
    print("Top selling Brand is :",top_brand.brandname)
    modellist=[]
    value_model=phonemodel.objects.annotate(Max('price'))
   
    arg = value_model.order_by('-price')
    argcount=arg.count()
      
    modellist.append(arg[0].id)
    for i in range(1,argcount):
        
        if(arg[i].price == arg[i-1].price):
            modellist.append(arg[i].id)
        else:
            break
    if(len(modellist) > 1):
        topvaluemodel=(phonemodel.objects.filter(id__in=modellist))
        topvaluemodel_count=topvaluemodel.count()
        print("Top Value Brand",topvaluemodel[0].brand_id)
    else:
        topvaluemodel=(phonemodel.objects.get(id=modellist[0]))
        topvaluemodel_count=1
        top_value_brand=topvaluemodel.brand_id.brandname
    print("Top valued brand",topvaluemodel.brand_id.brandname)
   
    return render(request,'list.html',{'phone_count':total_phone,'top_sell_brand':top_brand.brandname,'top_sell_model':modelobj,'top_model_count':modelobj_count,'top_value_model':topvaluemodel,'top_value_count':topvaluemodel_count,'top_value_brand':top_value_brand})
   
   