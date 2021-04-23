from __future__ import unicode_literals

from django.contrib import admin

from .models import Profile


class ProfiletAdmin(admin.ModelAdmin):
    fields = ['phone_number', 'birth_date', 'country', 'city', 'zip_code',
              'timezone', 'organization', 'address', 'website', 'avatar',
              'type_user', 'user']


admin.site.register(Profile, ProfiletAdmin)
