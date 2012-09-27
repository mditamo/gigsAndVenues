from genero.models import Genero, LikeGenero
from django.contrib import admin


class LikeGeneroAdmin(admin.ModelAdmin):
    list_display  = ('genero','usuario')

    
admin.site.register(Genero)
admin.site.register(LikeGenero, LikeGeneroAdmin)


