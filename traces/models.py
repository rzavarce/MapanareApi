from __future__ import unicode_literals
from djgeojson.fields import PointField
from django.db import models

from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Trace(models.Model):
    trace_type = models.CharField(max_length=15, verbose_name=_('Trace Type'))

    device = models.ForeignKey('devices.Device', verbose_name=_('Device'),
                               on_delete=models.CASCADE)

    gps_date = models.DateField(verbose_name=_('Date GPS'), null=True, )

    gps_time = models.TimeField(verbose_name=_('Time GPS'), null=True, )

    date_recieved = models.DateTimeField(verbose_name=_('Time Received'))

    timestamp = models.CharField(max_length=25, verbose_name=_('Tiemstamp'),
                                 blank=True, null=True, )

    geom = PointField(verbose_name=_('Coordinates'), blank=True, null=True, )

    gps_accuracy = models.IntegerField(verbose_name=_('GPS Accuracy'),
                                       blank=True, null=True, )

    speed = models.FloatField(verbose_name=_('Speed'), blank=True, null=True, )

    azimuth = models.CharField(max_length=6, verbose_name=_('Azimuth'),
                               blank=True, null=True, )

    odometer = models.FloatField(verbose_name=_('Odometer'), blank=True,
                                 null=True, )

    ignition_time_count = models.IntegerField(
        verbose_name=_('Ignition Time Count'), blank=True, null=True, )

    backup_battery = models.IntegerField(verbose_name=_('Backup Battery'),
                                         blank=True, null=True, )

    orientation = models.IntegerField(verbose_name=_('Orientation'), blank=True,
                                      null=True, )

    satellites_used = models.IntegerField(verbose_name=_('Satellites Used'),
                                          blank=True, null=True, )

    satellites_seen = models.IntegerField(verbose_name=_('Satellites Seen'),
                                          blank=True, null=True, )

    gprs_status = models.CharField(max_length=1, verbose_name=_('GPRS Status'),
                                   blank=True, null=True, )

    ignition = models.IntegerField(verbose_name=_('Ignition'), blank=True,
                                   null=True, )

    frame = models.CharField(max_length=255, verbose_name=_('Frame'),
                             blank=True, null=True, )

    altitude = models.CharField(max_length=255, verbose_name=_('Altitude'),
                                blank=True, null=True, )

    direction = models.TextField(verbose_name=_('Direction'), blank=True,
                                 null=True)

    created_date = models.DateTimeField(default=timezone.now,
                                        verbose_name=_('Created Date'))
    modified_date = models.DateTimeField(blank=True, null=True,
                                         verbose_name=_('Modified Date'))

    def __str__(self):
        return self.trace_type

    class Meta:
        verbose_name = _('Traces')
        verbose_name_plural = _('Traces')



