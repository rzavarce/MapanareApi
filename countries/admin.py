from __future__ import unicode_literals

from django.contrib import admin

from .models import Country


# Register your models here.

class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_code', 'country_name',)
    list_filter = ('country_name',)
    ordering = ('country_name',)
    search_fields = ('country_name',)


admin.site.register(Country, CountryAdmin)
