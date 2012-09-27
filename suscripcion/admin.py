from suscripcion.models import *
from django.contrib import admin

class SuscripcionGeneroAdmin(admin.ModelAdmin):
    list_display  = ('genero','usuario','periodicidad')
    
class SuscripcionComplejoAdmin(admin.ModelAdmin):
    list_display  = ('complejo','usuario','periodicidad')

class SuscripcionBandaAdmin(admin.ModelAdmin):
    list_display  = ('banda','usuario','periodicidad')

class SuscripcionMusicoAdmin(admin.ModelAdmin):
    list_display  = ('musico','usuario','periodicidad')
    
admin.site.register(Periodicidad)
admin.site.register(SuscripcionBanda,SuscripcionBandaAdmin)
admin.site.register(SuscripcionMusico,SuscripcionMusicoAdmin)
admin.site.register(SuscripcionComplejo, SuscripcionComplejoAdmin)
admin.site.register(SuscripcionGenero, SuscripcionGeneroAdmin)

