from django.shortcuts import render
import datetime,time
from .models import *
from datetime import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db.models import Q
from django.db.models import Avg,Sum,Count,Max
from django.contrib.auth.models import User, auth
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
#from .filters import modelFilter


# Create your views here.
def homepage(request):
    return render(request,'smartphone/mobilecenter.html')

def brandpage(request):
    return render(request,'smartphone/brand.html')
    
def createbrand(request):
    if request.method =='POST':
        try:   
            brandname=request.POST['brandname']
            brandfile=request.FILES['myfile']
            now = datetime.now()
            if(brandname =="" or brandfile==""):
                
                msg="Please fill required fields"
                return render(request,'smartphone/brand.html',{'msg':msg})
            else:
                savedata=brand(brandname=brandname,created_at=now,updated_at=now,brand_image=brandfile)
                savedata.save()
                msg="Data saved"
                return render(request,'smartphone/mobilecenter.html')
        except Exception as e:
            print("Some error occured")       
                 
                 
def modelpage(request):
    brandobj=brand.objects.all()
    
    return render(request,'smartphone/model.html',{'brandobj':brandobj})   

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
        return render(request,'smartphone/mobilecenter.html')
def brandlist(request):
        print("HELLO-----------")
        brandobj=brand.objects.all()
        paginator = Paginator(brandobj , 2)
        brandpage_number= request.GET.get("page")
        print("BRAND NO-----------------",brandpage_number)
        brandpageobj = paginator.get_page(brandpage_number)

        return render(request,'smartphone/listbrand.html',{'brandobj': brandpageobj})
def modellist(request):
        print("Haiiii")
        brand_id=request.GET['brand_id']
        modelobj=phonemodel.objects.filter(brand_id=brand_id)
        paginator = Paginator(modelobj , 3)
        page_number= request.GET.get('page')
        pageobj = paginator.get_page(page_number)
        print("Page :......",pageobj)
        return render(request,'smartphone/listmodel.html',{'modelobj': pageobj,'brand_id':brand_id})
        

def transaction(request):
        model_id=request.GET['model_id']
        
        modelobj=phonemodel.objects.get(id=model_id)
        
        
        return render(request,'smartphone/trans.html',{'modelobj': modelobj})
        
            
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
            return render(request,'smartphone/success.html',{'msg':msg})
        except Exception as e:
            print("Some Error occured")
def statistics(request):
    
    total_phone=mobile_trans.objects.count()
   
    TopValuedBrand = brand.objects.annotate(total_price=Sum('brand__price')).order_by('-total_price')[:1]
    print("Top Brand.........",TopValuedBrand[0].brandname)
    TopValuedModel = phonemodel.objects.annotate(max_price=Max('price')).order_by('-max_price').first()
    TopValuedModelobj=phonemodel.objects.filter(price=TopValuedModel.price)
    TopValuedModel_count=TopValuedModelobj.count()
    TopSellmodel = phonemodel.objects.annotate(mobilecount = Count('phonemodel')).order_by('-mobilecount').first()
    print("Top Sell Model is.......", TopSellmodel.modelname)
    TopSellBrand = brand.objects.annotate(brandcount=Count('brand__phonemodel')).order_by('-brandcount').first()
    print("Top Sell Brand is.......", TopSellBrand.brandname)
    result={
        'phone_count':total_phone,
        'TopSellBrand':TopSellBrand,
        'TopSellmodel':TopSellmodel,
        'TopValuedModel_count':TopValuedModel_count,
        'TopValuedModel':TopValuedModelobj,
        'top_value_brand':TopValuedBrand[0],
         'TopModel':TopValuedModel}
    return render(request,'smartphone/list.html',result)

def logout(request):
        auth.logout(request)
        return render(request,'accounts/login.html')