from disco.models import *
from django.contrib import admin

class ComposicionDiscoInline(admin.StackedInline):
    model = ComposicionDisco

class DiscoAdmin(admin.ModelAdmin):
    list_display  = ('nombre','discografica','fecha_publicacion')
    search_fields = ['nombre']
    inlines = [ComposicionDiscoInline]

admin.site.register(Tema)
admin.site.register(Disco,DiscoAdmin)



