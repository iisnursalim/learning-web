from django.contrib import admin
from .models import Jalan, Jembatan, Kesehatan, Drainase, Kab_Sidrap
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

class JalanAdm(LeafletGeoAdmin):
    #pass
    list_display = ('name', 'remark')

class JembatanAdm(LeafletGeoAdmin):
    #pass
    list_display = ('nama', 'tipe_jem')

class KesehatanAdm(LeafletGeoAdmin):
    #pass
    list_display = ('namobj', 'remark')

class DrainaseAdm(LeafletGeoAdmin):
    #pass
    list_display = ('lcode', 'rpru')

class SidrapAdm(LeafletGeoAdmin):
    #pass
    list_display = ('kecamatan', 'desa')

admin.site.register(Jembatan, JembatanAdm)
admin.site.register(Jalan, JalanAdm)
admin.site.register(Kesehatan, KesehatanAdm)
admin.site.register(Drainase, DrainaseAdm)
admin.site.register(Kab_Sidrap, SidrapAdm)
