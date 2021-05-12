from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Music

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']
 

class MusicForm(forms.ModelForm):  
    class Meta:  
        model = Music
        fields = ['name', 'album', 'artista', 'year','genero'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 'name': forms.TextInput(attrs={ 'class': 'form-control' }), 
                    'album': forms.TextInput(attrs={ 'class': 'form-control' }),
                    'artista': forms.TextInput(attrs={ 'class': 'form-control' }),
                    'year': forms.TextInput(attrs={ 'class': 'form-control' }),
                    'genero': forms.TextInput(attrs={ 'class': 'form-control' }),
      }

class UpgradeAccountForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','password']