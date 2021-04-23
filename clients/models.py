from django.db import models
from django.utils.translation import gettext_lazy as _
import pytz
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

STATUS = (('0', _('Inactive')), ('1', _('Active')))


class Client(models.Model):
    user = models.ManyToManyField('auth.User', verbose_name=_('User'),
                                  blank=True)
    commercial_name = models.CharField(max_length=255,
                                       verbose_name=_('Commercial Name'))
    cif = models.CharField(max_length=20, verbose_name=_('CIF Number'))
    commercial_email = models.EmailField(max_length=150,
                                         verbose_name=_('Commercial Email'))
    phone_number = PhoneNumberField(verbose_name=_('Phone Number'), blank=True)
    address = models.CharField(max_length=255, verbose_name=_('Address'),
                               blank=True)
    zip_code = models.IntegerField(verbose_name=_('Zip Code'), null=True)
    country = models.ForeignKey('countries.Country', verbose_name=_('Country'),
                                on_delete=models.CASCADE, null=True)
    city = models.CharField(max_length=150, verbose_name=_('City'), null=True)
    avatar = models.ImageField(upload_to='uploads/images/avatars/',
                               verbose_name=_('Avatar'), blank=True)
    website = models.URLField(verbose_name=_('Website'), blank=True)

    description = models.TextField(verbose_name=_('Description'), blank=True)
    status = models.CharField(max_length=150, choices=STATUS,
                              verbose_name=_('Status'))
    created_date = models.DateTimeField(default=timezone.now,
                                        verbose_name=_('Created Date'))
    modified_date = models.DateTimeField(blank=True, null=True,
                                         verbose_name=_('Modified Date'))

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.commercial_name

    class Meta:
        verbose_name = _('Client')
        verbose_name_plural = _('Clients')
