from __future__ import unicode_literals

from django.contrib import admin

from .models import VehiclesGroup


# Register your models here.

class VehiclesGroupAdmin(admin.ModelAdmin):
    # list_display = ('nickname', 'registration_number', 'aircraft_model',
    # 'aircraft_serie', 'created_date',)
    # list_filter = ('nickname', 'registration_number',)
    # ordering = ('nickname',)
    # search_fields = ('registration_number',)

    fields = ['nickname', 'description', 'color', 'status', 'user', 'vehicles']


admin.site.register(VehiclesGroup, VehiclesGroupAdmin)