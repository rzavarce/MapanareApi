from __future__ import unicode_literals

# from django.contrib import admin

from .models import Trace
from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin


class TraceAdmin(admin.ModelAdmin):
    list_display = ('device_imei', 'date_recieved', 'coordinates',
                    'satellites_used', 'num_modules',)
    list_filter = ('device_imei', 'date_recieved',)
    ordering = ('date_created',)
    search_fields = ('device_imei', 'date_recieved',)

    fields = ['trace_type', 'device_imei', 'date_sended', 'date_recieved',
              'timestamp', 'geom', 'gps_accuracy', 'speed', 'azimuth',
              'odometer', 'ignition_time_count', 'backup_battery',
              'orientation', 'satellites_used', 'satellites_seen',
              'gprs_status', 'ignition', 'frame', ]


admin.site.register(Trace, LeafletGeoAdmin)
