from __future__ import unicode_literals

from django.contrib import admin

from .models import Device


# Register your models here.

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_imei', 'sim_phone', 'type_device', 'model_device',
                    'status',)
    list_filter = ('device_imei', 'type_device', 'model_device', 'status',)
    ordering = ('device_imei',)
    search_fields = ('device_imei',)

    fields = ['device_imei', 'sim_phone', 'password', 'type_device',
              'model_device', 'firmware_device', 'status', 'description',
              'user', ]


admin.site.register(Device, DeviceAdmin)
