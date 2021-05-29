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
    path('', login_view, name="login"),
    path('logout/', login_view, name="logout"),
    path('register/', register_view, name="register"),
    path('edashboard/', index, name='edashboard'),  
    path('addnew',addnew),  
    path('edit/<int:id>', edit),  
    path('update/<int:id>', update),  
    path('delete/<int:id>', destroy),
    path('udashboard/', index2, name='udashboard'),  
    path('addnew2',addnew2),  
    path('edit2/<int:id>', edit2),  
    path('update2/<int:id>', update2),  
    path('delete2/<int:id>', destroy2),
    path('informacion/',informaciont, name='informacion'),
    path('contacto/',contacto, name="contacto"),
    path('manual/', manual, name='manual'),
    path('contactoo/', contacto2, name="contacto2")




]
