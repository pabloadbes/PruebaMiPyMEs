from django.contrib import admin
from .models import Encuesta, Pregunta, Seccion
# Register your models here.

class EncuestaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class SeccionAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PreguntaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('order', 'name', 'seccion')
    ordering = ('order','updated')
    search_fields = ('order', 'name', 'content', 'seccion__name')
    date_hierarchy = 'updated'
    list_filter = ('seccion__name', 'name')

   #  def post_categories(self, obj):
   #      return ", ".join([c.name for c in obj.categories.all().order_by("name")])
   #  post_categories.short_description = "Categorías"
    
admin.site.register(Encuesta, EncuestaAdmin)
admin.site.register(Seccion, SeccionAdmin)
admin.site.register(Pregunta, PreguntaAdmin)