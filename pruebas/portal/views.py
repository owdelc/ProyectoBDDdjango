from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import connection 

from .models import *
from .forms import CustomUserCreationForm, ReportsForm

# Create your views here.
# Parte Oscar
# Login y roles

def register_view(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created succesfully!')
            return redirect('login')
    context = {'form':form}
    return render(request, 'register.html', context)


def login_view(request):
    form = AuthenticationForm()
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_expert==True:
            login(request, user)
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            else:
                return redirect('edashboard')
        if user is not None and user.is_expert==False:
            login(request, user)
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            else:
                return redirect('udashboard')
        
        
    return render(request, 'login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')





#Aqui empieza parte de Hugo
# Tabla artista
def addnew(request):  
    if request.method == "POST":  
        form = ReportsForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('edashboard')  
            except:  
                pass 
    else:  
        form = ReportsForm()  
    return render(request,'artista/index.html',{'form':form})  
def index(request):  
    reports = Reports.objects.all()  
    return render(request,"artista/show.html",{'reports':reports})  

def edit(request, id):  
    song = Reports.objects.get(id=id)  
    return render(request,'artista/edit.html', {'song':song})  

def update(request, id):  
    song = Reports.objects.get(id=id)  
    form = ReportsForm(request.POST, instance = song)  
    if form.is_valid():  
        form.save()  
        return redirect("edashboard")  
    return render(request, 'artista/edit.html', {'song': song}) 
     
def destroy(request, id):  
    song = Reports.objects.get(id=id)
    if request.method == "POST":
        song.delete()  
        return redirect("edashboard")  

    return render(request,'artista/delete.html')

#Tabla usuario suscrito

def addnew2(request):  
    if request.method == "POST":  
        form = ReportsForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('udashboard')  
            except:  
                pass 
    else:  
        form = ReportsForm()  
    return render(request,'usuario/index.html',{'form':form})  
def index2(request):  
    reports = Reports.objects.all()  
    return render(request,"usuario/show.html",{'reports':reports})  

def edit2(request, id):  
    song = Reports.objects.get(id=id)  
    return render(request,'usuario/edit.html', {'song':song})  

def update2(request, id):  
    song = Reports.objects.get(id=id)  
    form = ReportsForm(request.POST, instance = song)  
    if form.is_valid():  
        form.save()  
        return redirect("udashboard")  
    return render(request, 'usuario/edit.html', {'song': song})  
def destroy2(request, id):  
    song = Reports.objects.get(id=id)  
    song.delete()  
    return redirect("udashboard") 


def informaciont(request):
    return render(request,'usuario/extras/info.html')

def manual(request):
    return render(request,'usuario/extras/manual.html')

def contacto(request):
    return render(request,'usuario/extras/contacto.html')
# Seccion de reporteria
