from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import connection 

from .models import *
from .forms import CustomUserCreationForm, MusicForm, UpgradeAccountForm

# Create your views here.
# Parte Oscar
# Login y roles
def free_home_view(request):
    date_today = datetime.now().date()
    return render(request,'free_user.html', {'date_today':date_today})

def suscribed_home_view(request):
    date_today = datetime.now().date()
    return render(request,'suscribed_home.html', {'date_today':date_today})

def artist_home_view(request):
    date_today = datetime.now().date()
    return render(request,'artist_home.html', {'date_today':date_today})

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
        if user is not None and user.is_suscribed==True:
            login(request, user)
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            else:
                return redirect('udashboard')
        if user is not None and user.is_artist==True:
            login(request, user)
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            else:
                return redirect('adashboard')
        if user is not None and user.is_suscribed==False and user.is_artist==False:
            login(request, user)
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            else:
                return redirect('undashboard')
    return render(request, 'login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')

def suscribe(request):
    form = AuthenticationForm()
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_suscribed==False:
            user.is_suscribed=True
            user.save()
            return redirect('udashboard')

    return render(request, 'unsuscribed/suscribe/suscribe.html', {'form':form})

def becomeArtist(request):
    form = AuthenticationForm()
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_artist==False:
            user.is_artist=True
            user.save()
            return redirect('adashboard')

    return render(request, 'unsuscribed/suscribe/becomeArtist.html', {'form':form})



#Aqui empieza parte de Hugo
# Tabla artista
def addnew(request):  
    if request.method == "POST":  
        form = MusicForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('adashboard')  
            except:  
                pass 
    else:  
        form = MusicForm()  
    return render(request,'artista/index.html',{'form':form})  
def index(request):  
    songs = Music.objects.all()  
    return render(request,"artista/show.html",{'songs':songs})  

def edit(request, id):  
    song = Music.objects.get(id=id)  
    return render(request,'artista/edit.html', {'song':song})  

def update(request, id):  
    song = Music.objects.get(id=id)  
    form = MusicForm(request.POST, instance = song)  
    if form.is_valid():  
        form.save()  
        return redirect("adashboard")  
    return render(request, 'artista/edit.html', {'song': song})  
def destroy(request, id):  
    song = Music.objects.get(id=id)  
    song.delete()  
    return redirect("adashboard")  

#Tabla usuario suscrito

def addnew2(request):  
    if request.method == "POST":  
        form = MusicForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('udashboard')  
            except:  
                pass 
    else:  
        form = MusicForm()  
    return render(request,'usuario/index.html',{'form':form})  
def index2(request):  
    songs = Music.objects.all()  
    return render(request,"usuario/show.html",{'songs':songs})  

def edit2(request, id):  
    song = Music.objects.get(id=id)  
    return render(request,'usuario/edit.html', {'song':song})  

def update2(request, id):  
    song = Music.objects.get(id=id)  
    form = MusicForm(request.POST, instance = song)  
    if form.is_valid():  
        form.save()  
        return redirect("udashboard")  
    return render(request, 'usuario/edit.html', {'song': song})  
def destroy2(request, id):  
    song = Music.objects.get(id=id)  
    song.delete()  
    return redirect("udashboard") 

# Tabla usuario freemium
def addnew3(request):  
    if request.method == "POST":  
        form = MusicForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('undashboard')  
            except:  
                pass 
    else:  
        form = MusicForm()  
    return render(request,'unsuscribed/index.html',{'form':form})  
def index3(request):  
    songs = Music.objects.all()  
    return render(request,"unsuscribed/show.html",{'songs':songs})  

def edit3(request, id):  
    song = Music.objects.get(id=id)  
    return render(request,'unsuscribed/edit.html', {'song':song})  

def update3(request, id):  
    song = Music.objects.get(id=id)  
    form = MusicForm(request.POST, instance = song)  
    if form.is_valid():  
        form.save()  
        return redirect("undashboard")  
    return render(request, 'unsuscribed/edit.html', {'song': song})  
def destroy3(request, id):  
    song = Music.objects.get(id=id)  
    song.delete()  
    return redirect("undashboard") 


# Seccion de reporteria

def query1(request):
    if request.method=='POST':
        desdefecha = request.POST.get('desdefecha')
        hastafecha = request.POST.get('hastafecha') 
        resultado = ReproduccionesModel.objects.raw("select id,name, album, artista, count(name) as total from reproducciones where fecha between '"+desdefecha+"' and '"+hastafecha+"' group by id, name,album,artista order by total DESC")
        return render(request, 'prueba.html', {'data':resultado})
    else:
        resultado = ReproduccionesModel.objects.raw('select id,name, album, artista, count(name) as total from reproducciones group by id, name,album, artista order by total DESC')
        return render(request,"prueba.html",{'data':resultado})
        

def query2(request):
    if request.method=='POST':
        desdefecha = request.POST.get('desdefecha')
        hastafecha = request.POST.get('hastafecha') 
        limite = request.POST.get('limitador')
        resultado = ReproduccionesModel.objects.raw("select id,artista, count(name) as total from reproducciones where fecha between '"+desdefecha+"' and '"+hastafecha+"' group by id, artista order by total DESC LIMIT '"+limite+"'")
        return render(request, 'prueba2.html', {'data':resultado})
    else:
        resultado = ReproduccionesModel.objects.raw('select id,name, album, artista, count(name) as total from reproducciones group by id, name,album, artista order by total DESC')
        return render(request,"prueba2.html",{'data':resultado})


def query3(request):
    if request.method=='POST':
        desdefecha = request.POST.get('desdefecha')
        hastafecha = request.POST.get('hastafecha') 
        resultado = ReproduccionesModel.objects.raw("select id,genero, count(name) as total from reproducciones where fecha between '"+desdefecha+"' and '"+hastafecha+"' group by id, genero order by total DESC")
        return render(request, 'prueba2.html', {'data':resultado})
    else:
        resultado = ReproduccionesModel.objects.raw('select id,genero, count(name) as total from reproducciones group by id, genero order by total DESC')
        return render(request,"prueba3.html",{'data':resultado})



def addnew4(request):  
    if request.method == "POST":  
        form = MusicForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('undashboard')  
            except:  
                pass 
    else:  
        form = MusicForm()  
    return render(request,'reporteria/index.html',{'form':form})  
def index4(request):  
    songs = Music.objects.all().order_by('-reprodu')
    return render(request,"reporteria4/show.html",{'songs':songs})  

def edit4(request, id):  
    song = Music.objects.get(id=id)  
    return render(request,'reporteria4/edit.html', {'song':song})  

def update4(request, id):  
    song = Music.objects.get(id=id)  
    form = MusicForm(request.POST, instance = song)  
    if form.is_valid():  
        form.save()  
        return redirect("undashboard")  
    return render(request, 'reporteria4/edit.html', {'song': song})  
def destroy4(request, id):  
    song = Music.objects.get(id=id)  
    song.delete()  
    return redirect("undashboard") 

def addnew5(request):  
    if request.method == "POST":  
        form = MusicForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('undashboard')  
            except:  
                pass 
    else:  
        form = MusicForm()  
    return render(request,'reporteria/index.html',{'form':form})  
def index5(request):  
    songs = PlaylistModel.objects.all()
    return render(request,"playlist/show.html",{'songs':songs})  

def edit5(request, id):  
    song = Music.objects.get(id=id)  
    return render(request,'playlist/edit.html', {'song':song})  

def update5(request, id):  
    song = Music.objects.get(id=id)  
    form = MusicForm(request.POST, instance = song)  
    if form.is_valid():  
        form.save()  
        return redirect("undashboard")  
    return render(request, 'playlist/edit.html', {'song': song})  
def destroy5(request, id):  
    song = Music.objects.get(id=id)  
    song.delete()  
    return redirect("undashboard") 

def regalias(request):
    return render(request, 'artista/regalias.html')