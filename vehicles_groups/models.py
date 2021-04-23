from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

from django.utils.translation import gettext_lazy as _

STATUS = (('0', _('Inactive')), ('1', _('Active')))


class VehiclesGroup(models.Model):
    nickname = models.CharField(max_length=150, verbose_name=_('Nickname'))

    description = models.TextField(verbose_name=_('Description'))
    color = models.CharField(max_length=150, blank=True,
                             verbose_name=_('Color'))
    status = models.CharField(max_length=150, choices=STATUS,
                              verbose_name=_('Status'))

    user = models.ForeignKey('auth.User', verbose_name=_('User'), blank=True,
                             null=True, on_delete=models.CASCADE, )

    vehicles = models.ManyToManyField('vehicles.Vehicles',
                                      verbose_name=_('Vehicles'), blank=True)

    created_date = models.DateTimeField(default=timezone.now,
                                        verbose_name=_('Created Date'))
    modified_date = models.DateTimeField(blank=True, null=True,
                                         verbose_name=_('Modified Date'))

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = _('Vehicle Group')
        verbose_name_plural = _('Vehicle Groups')