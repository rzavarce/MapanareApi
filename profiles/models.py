from django.db import models

from django.utils.translation import gettext_lazy as _

from timezone_field import TimeZoneField
from phonenumber_field.modelfields import PhoneNumberField

from django.conf import settings

AGE = [(x, x) for x in range(18, 66)]
TYPE_USER = (('1',_('Client')),('2',_('User Query')),('3',_('Mechanic')),
             ('4',_('Pilot')),('5',_('Technicnas')))


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, unique=True,
                                related_name='profile',
                                on_delete=models.CASCADE)
    address = models.CharField(max_length=255, verbose_name=_('Address'),
                               blank=True)
    avatar = models.ImageField(upload_to='uploads/images/avatars/',
                               verbose_name=_('Avatar'), blank=True,)
    birth_date = models.DateField(verbose_name=_('Birth Date'),
                                  blank=True, null=True)
    city = models.CharField(max_length=150, verbose_name=_('City'), null=True)
    country = models.ForeignKey('countries.Country', verbose_name=_('Country'),
                                on_delete=models.CASCADE, null=True)
    organization = models.CharField(max_length=150,
                                    verbose_name=_('Organization'), blank=True)
    phone_number = PhoneNumberField(verbose_name=_('Phone Number'), blank=True)
    timezone = TimeZoneField(verbose_name=_('Time Zone'), null=True)
    website = models.URLField(verbose_name=_('Website'), blank=True)
    zip_code = models.IntegerField(verbose_name=_('Zip Code'), null=True)
    nickname = models.CharField(max_length=150, verbose_name=_('Nickname'),
                                null=True)
    age = models.IntegerField(choices=AGE, verbose_name=_('Age'),null=True)
    type_user = models.CharField(max_length=15, choices=TYPE_USER,
                                 verbose_name=_('Status'), default=1)
    activation_token = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(blank=True, null=True)
