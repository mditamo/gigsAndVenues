from evento.models import Evento, AsistenciaFan
from django.contrib import admin


class EventoAdmin(admin.ModelAdmin):
    list_display  = ('nombre','fecha','hora_inicio', 'descripcion')
    search_fields = ['nombre']
    
admin.site.register(Evento,EventoAdmin)
admin.site.register(AsistenciaFan)