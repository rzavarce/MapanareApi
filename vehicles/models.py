from __future__ import unicode_literals
from django.db import models
from django import forms
from django.utils import timezone
from django.core.validators import MaxValueValidator
from simple_history.models import HistoricalRecords
from django.utils.translation import gettext_lazy as _

TYPE = (('TYPE01', 'TYPE01'),
             ('TYPE02', 'TYPE02'),
             ('TYPE03', 'TYPE03'),
             ('TYPE04', 'TYPE04'),
             )

CATEGORY = (('Electric', 'Electric'),
                 ('Scooter', 'Scooter'),
                 ('Motocross', 'Motocross'),
                 ('Enduro', 'Enduro'),
                 ('Trial', 'Trial'),
                 ('Trail', 'Trail'),
                 ('Cruiser', 'Cruiser'),
                 ('Chopper', 'Chopper'),
                 ('Great Tourism', 'Great Tourism'),
                 ('Racer', 'Racer'),
                 )

ENGINE_TYPE = (('Single Cylinder', 'Single Cylinder'),
               ('Two Cylinder', 'Two Cylinder'),
               ('Three Cylinder', 'Three Cylinder'),
               ('Tetra Cylindrical', 'Tetra Cylindrical'),
               )

FUEL_TYPE = (('FULL_TYPE01', 'FULL_TYPE01'),
             ('FULL_TYPE02', 'FULL_TYPE02'),
             ('FULL_TYPE03', 'FULL_TYPE03'),
             ('FULL_TYPE04', 'FULL_TYPE04'),
             )

STATUS = ((0, _('Inactive')), (1, _('Active')))

STATUS_DRY = (
("Ign OFF", _("Ign OFF")), ("Ign ON", _("Ign ON")), ("Driving", _("Driving")),
("W/o Coverage", _("W/o Coverage")))

ENGINE_NUMBERS = ((0, '0'), (1, '1'),)


class Vehicles(models.Model):
    nickname = models.CharField(max_length=150, verbose_name=_('Nickname'))
    type = models.CharField(max_length=150, choices=TYPE,
                            verbose_name=_('Type'))
    category = models.CharField(max_length=150, choices=CATEGORY,
                                verbose_name=_('Category'))
    model = models.CharField(blank=True, null=True, max_length=150,
                             verbose_name=_('Model'))
    serie = models.CharField(blank=True, null=True, max_length=150,
                             verbose_name=_('Serie'))
    registration_number = models.CharField(
        blank=True, null=True, max_length=150,
        verbose_name=_('Registration Number'))
    manufacturing_year = models.PositiveIntegerField(
        blank=True, null=True, verbose_name=_('Manufacturing Year'))
    manufacturer = models.CharField(blank=True, null=True, max_length=150,
                                    verbose_name=_('Manufacturer'))
    engine_type = models.CharField(blank=True, null=True, max_length=150,
                                   choices=ENGINE_TYPE,
                                   verbose_name=_('Engines Type'))
    engine_model = models.CharField(blank=True, null=True, max_length=150,
                                    verbose_name=_('Engines Model'))
    fuel_type = models.CharField(blank=True, null=True, max_length=150,
                                 choices=FUEL_TYPE, verbose_name=_('Fuel Type'))
    fuel_capacity = models.PositiveIntegerField(blank=True, null=True,
                                                verbose_name=_('Fuel Capacity'))
    fuel_autonomy = models.PositiveIntegerField(blank=True, null=True,
                                                verbose_name=_('Fuel Autonomy'))

    number_seats = models.PositiveIntegerField(blank=True, null=True,
                                               verbose_name=_('Number Seats'))

    description = models.TextField(blank=True, null=True,
                                   verbose_name=_('Description'))

    status = models.BooleanField(default=False, verbose_name=_('Status'))

    status_dry = models.CharField(blank=True, null=True, max_length=150,
                                  default="Ign OFF",
                                  choices=STATUS_DRY,
                                  verbose_name=_('Status Drive'))

    device = models.OneToOneField('devices.Device', verbose_name=_('Devices'),
                                  on_delete=models.PROTECT, blank=True,
                                  null=True, )

    client = models.ForeignKey('clients.Client', verbose_name=_('Client'),
                               blank=True, null=True,
                               on_delete=models.CASCADE, )

    history = HistoricalRecords()

    created_date = models.DateTimeField(default=timezone.now,
                                        verbose_name=_('Created Date'))
    modified_date = models.DateTimeField(blank=True, null=True,
                                         verbose_name=_('Modified Date'))

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = _('Vehicle')
        verbose_name_plural = _('Vehicles')







