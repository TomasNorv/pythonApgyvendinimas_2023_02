from django.contrib import admin
from .models import Objektas



# Register your models here.
class ObjektasAdmin(admin.ModelAdmin):
    list_display = ('caption', 'type', 'city', 'area', 'rooms', 'max_guest')
    list_filter = ('type', 'city')
    search_fields = ['type','city']


admin.site.register(Objektas, ObjektasAdmin)
