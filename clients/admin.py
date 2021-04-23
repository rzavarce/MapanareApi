from __future__ import unicode_literals

from django.contrib import admin

from .models import Client


# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display = ('commercial_name', 'cif', 'commercial_email', 'status', 'created_date',)
    list_filter = ('commercial_name', 'commercial_email',)
    ordering = ('commercial_name',)
    search_fields = ('commercial_name','commercial_email')

    fields = ['commercial_name', 'cif', 'commercial_email', 'phone_number', 'address', 'zip_code', 'country', 'city', 'avatar', 'website', 'description', 'status', 'user', ]


admin.site.register(Client, ClientAdmin)
