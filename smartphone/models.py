from django.db import models
from django.db import models
from django.contrib.auth.models import User

T_TYPE=(
        ('Cash','Cash'),
        ('Card','Card'),
) 
class brand(models.Model):
    brandname=models.CharField(max_length=200,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    brand_image=models.ImageField(upload_to='brandimg/', default=None,null=True)


class phonemodel(models.Model):
    brand_id=models.ForeignKey(brand, on_delete=models.CASCADE, null=True,related_name="brand")
    modelname=models.CharField(max_length=200,null=True)
    release_year=models.DateField()
    available_quantities=models.IntegerField()
    price=models.DecimalField( max_digits = 10, decimal_places = 2) 
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_available=models.BooleanField()
    mobile_image=models.ImageField(upload_to='mobimg/', default=None,null=True)

class mobile_trans(models.Model):
    usersample=models.ForeignKey(User, on_delete=models.CASCADE) 
    trans_model=models.ForeignKey(phonemodel,on_delete=models.CASCADE,null=True,related_name="phonemodel")
    transaction_type=models.CharField(choices=T_TYPE,max_length=20,null=True)
    t_amount=models.IntegerField()


# Create your models here.
