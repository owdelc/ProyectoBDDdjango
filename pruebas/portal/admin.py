from django.contrib import admin
from django.apps import *
from .models import *
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin
from simple_history.admin import SimpleHistoryAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    list_filter=("is_expert",)

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User role',
            {
                'fields': (
                    'is_expert',
                )
            }
        )
    )





admin.site.register(CustomUser, CustomUserAdmin)







