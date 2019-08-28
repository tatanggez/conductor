from django.contrib import admin
from apps.conductor.models import Tvehiculo
from apps.conductor.models import Tlicencia
from apps.conductor.models import FichaConductor

admin.site.register(FichaConductor)
admin.site.register(Tvehiculo)
admin.site.register(Tlicencia)
# Register your models here.
