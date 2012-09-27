from complejo.models import *
from django.contrib import admin
from sede.models import Sede

class SedeInline(admin.StackedInline):
    model = Sede

class ComplejoAdmin(admin.ModelAdmin):
    fieldsets = [(None,{'fields':['nombre']})]
    #search_fields = ['nombre']
    inlines = [SedeInline]

admin.site.register(Complejo,ComplejoAdmin)

