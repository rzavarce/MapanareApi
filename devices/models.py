# Create your models here.
from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

from django.utils.translation import gettext_lazy as _

TYPES_DEVICE = (('GPS_Inside', 'GPS_Inside'), ('Arduino', 'Arduino'),)

MODELS_DEVICE = (('MDU001', 'MDU001'), ('MDU002', 'MDU002'),)

FIRMWARES_DEVICE = (('MDU002_001', 'MDU002_001'), ('MDU002_002', 'MDU002_002'),
                    ('MDU002_003', 'MDU002_003'),)

STATUS = (('0', _('Active')), ('1', _('Inactive')))


class Device(models.Model):
    device_imei = models.BigIntegerField(verbose_name=_('Imei'))

    sim_phone = models.CharField(max_length=15, verbose_name=_('SIM Phone'))

    password = models.IntegerField(verbose_name=_('Password'))

    type_device = models.CharField(max_length=15, choices=TYPES_DEVICE,
                                   verbose_name=_('Type Device'))

    model_device = models.CharField(max_length=15, choices=MODELS_DEVICE,
                                    verbose_name=_('Model Device'))

    firmware_device = models.CharField(max_length=15, choices=FIRMWARES_DEVICE,
                                       verbose_name=_('Firmware Device'))

    status = models.CharField(max_length=15, choices=STATUS,
                              verbose_name=_('Status'))

    description = models.TextField(verbose_name=_('Description'))

    user = models.ForeignKey('auth.User', verbose_name=_('User'), blank=True,
                             null=True, on_delete=models.CASCADE, )

    created_date = models.DateTimeField(default=timezone.now,
                                        verbose_name=_('Created Date'))

    modified_date = models.DateTimeField(blank=True, null=True,
                                         verbose_name=_('Modified Date'))

    unit_id = models.IntegerField(verbose_name=_('ID Unit'), blank=True,
                                  null=True, )

    def __str__(self):
        return str(self.device_imei)

    class Meta:
        verbose_name = _('Devices')
        verbose_name_plural = _('Devices')
