
from django.contrib import admin
from django.urls import path
from.import views


urlpatterns = [
    
    path("register",views.register,name='registration'),
    path("index",views.index,name='index'),
    path("registration",views.registration,name='userreg'),
    path("login",views.login,name='login')
      ]
