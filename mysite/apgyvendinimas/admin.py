from django.contrib import admin
from .models import Objektas



# Register your models here.
class ObjektasAdmin(admin.ModelAdmin):
    list_display = ('caption', 'type', 'city', 'area', 'rooms', 'max_guest')

admin.site.register(Objektas, ObjektasAdmin)
