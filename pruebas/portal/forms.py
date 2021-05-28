from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Reports

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']
 

class ReportsForm(forms.ModelForm):
    class Meta:  
        model = Reports
        fields = ['especie', 'lugar', 'region','link','ubicacion'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 'especie': forms.TextInput(attrs={ 'class': 'form-control' }), 
                    'lugar': forms.TextInput(attrs={ 'class': 'form-control' }),
                    'region': forms.TextInput(attrs={ 'class': 'form-control' }),
                    'link': forms.TextInput(attrs={ 'class': 'form-control' }),
                    'ubicacion': forms.TextInput(attrs={ 'class': 'form-control' }),
        }


class UpgradeAccountForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','password']