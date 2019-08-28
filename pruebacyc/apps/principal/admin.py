from django.contrib import admin
class UbicacionAdmin(admin.ModelAdmin):
    readonly_fields = ('hora','fecha')

class UbicacionFinalAdmin(admin.ModelAdmin):
    readonly_fields = ('hora','fecha')

from apps.principal.models import Ubicacion, UbicacionFinal

admin.site.register(Ubicacion,UbicacionAdmin)
admin.site.register(UbicacionFinal,UbicacionFinalAdmin)
# Register your models here.
