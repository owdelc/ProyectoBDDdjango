"""pruebas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from portal.views import *

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('fhome/', free_home_view, name="free-home"),
    path('shome/', suscribed_home_view, name="sus-home"),
    path('ahome/', artist_home_view, name="arti-home"),
    path('', login_view, name="login"),
    path('logout/', login_view, name="logout"),
    path('register/', register_view, name="register"),
    path('adashboard/', index, name='adashboard'),  
    path('addnew',addnew),  
    path('edit/<int:id>', edit),  
    path('update/<int:id>', update),  
    path('delete/<int:id>', destroy),
    path('udashboard/', index2, name='udashboard'),  
    path('addnew2',addnew2),  
    path('edit2/<int:id>', edit2),  
    path('update2/<int:id>', update2),  
    path('delete2/<int:id>', destroy2),
    path('undashboard/', index3, name='undashboard'),  
    path('addnew3',addnew3),  
    path('edit3/<int:id>', edit3),  
    path('update3/<int:id>', update3),  
    path('delete3/<int:id>', destroy3),


]
