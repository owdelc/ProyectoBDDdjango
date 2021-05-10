from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User role',
            {
                'fields': (
                    'is_suscribed',
                    'is_artist',
                    'is_moderatorA',
                    'is_moderatorB',
                )
            }
        )
    )

admin.site.register(CustomUser, CustomUserAdmin)