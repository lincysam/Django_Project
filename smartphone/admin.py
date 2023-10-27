from django.contrib import admin

# Register your models here.
from .models import brand
admin.site.register (brand)
from .models import phonemodel
admin.site.register (phonemodel)