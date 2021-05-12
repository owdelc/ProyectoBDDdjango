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
    list_filter=("is_suscribed", "is_artist")

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


class MusicAdmin(admin.ModelAdmin):
    list_display=("name", "album", "artista", "genero")
    search_fields=("name", "album", "artista", "genero")
    list_filter=("genero", "year")


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Music,MusicAdmin)
admin.site.register(PlaylistModel)



class HistoricalCustomUserAdmin(admin.ModelAdmin):
    list_display=("username", "history_date", "history_type")
    search_fields=("history_date", "history_type")
    list_filter=("history_date", "history_type")

class HistoricalMusicAdmin(admin.ModelAdmin):
    list_display=("name", "artista", "history_date", "history_type")
    search_fields=("history_date", "history_type")
    list_filter=("history_date", "history_type")

HistoricalCustomModel = apps.get_model("portal", "HistoricalCustomUser")

admin.site.register(HistoricalCustomModel,HistoricalCustomUserAdmin)

HistoricalCustomModel2 = apps.get_model("portal", "HistoricalMusic")

admin.site.register(HistoricalCustomModel2,HistoricalMusicAdmin)

admin.site.register(ReproduccionesModel)



