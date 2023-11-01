from django.contrib import admin

# Register your models here.
from .models import brand
admin.site.register (brand)
from .models import phonemodel
admin.site.register (phonemodel)
from .models import mobile_trans
admin.site.register(mobile_trans)