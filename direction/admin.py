from django.contrib import admin
from .models import Direction, Service


# Register your models here.

class DirectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'alias': ('abreviation',)}
    list_display = ('abreviation', 'alias', 'direction_nom')


class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'alias': ('abreviation',)}
    list_display = ('abreviation', 'service_nom', 'direction')


admin.site.register(Direction, DirectionAdmin)
admin.site.register(Service, ServiceAdmin)
