from __future__ import unicode_literals

from django.contrib import admin

from .models import Vehicles


# Register your models here.

class VehiclesAdmin(admin.ModelAdmin):
    list_display = ( 'nickname', 'registration_number', 'model', 'serie',
                     'created_date',)
    list_filter = ('nickname', 'registration_number',)
    ordering = ('nickname',)
    search_fields = ('registration_number',)

    fields = ['nickname', 'type', 'category', 'model',
              'serie', 'registration_number',
              'number_seats', 'manufacturing_year', 'manufacturer',
              'engines_type', 'engines_models', 'fuel_type',
              'fuel_capacity', 'fuel_autonomy', 'description', 'status',
              'client', 'device']


admin.site.register(Vehicles, VehiclesAdmin)
