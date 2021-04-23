from __future__ import unicode_literals

from django.db import models


class Country(models.Model):
    country_code = models.CharField(max_length=2)
    country_name = models.CharField(max_length=50)

    def __str__(self):
        return self.country_name
