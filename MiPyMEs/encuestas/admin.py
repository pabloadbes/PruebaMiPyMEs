from django.contrib import admin
from .models import Encuesta

# Register your models here.
class EncuestaAdmin(admin.ModelAdmin):
    list_display = ('name', 'subtitle')

admin.site.register(Encuesta, EncuestaAdmin)
