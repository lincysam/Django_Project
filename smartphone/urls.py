"""
URL configuration for newshowroom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from.import views






urlpatterns = [

    #path('admin/', admin.site.urls),
    path("home",views.homepage,name='home'),
    path("brand",views.brandpage,name='brand'),
    path("createbrand",views.createbrand,name='brand'),
    path("model",views.modelpage,name='model'),
    path("createmodel",views.createmodel,name='brand'),
    path("listbrands",views.brandlist,name='brandlist'),
    path("modellist/",views.modellist,name='modellist'),
    path("transaction",views.transaction,name='trans'),
    path("payment",views.payment,name='trans'),
    path("statistics",views.statistics,name='status'),
    path("logout",views.logout,name='logout')

    #path("updatemodel/<int:pk>",views.updatemodel,'update')
      ]
