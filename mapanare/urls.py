"""mapanare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.conf.urls import url

from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

PREFIX_API = "api/v1/"

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    # path('admin/', admin.site.urls),
    path('baton/', include('baton.urls')),

    # JWT auth
    # url(PREFIX_API + "/auth/obtain_token/", obtain_jwt_token),
    url(PREFIX_API + 'auth-jwt/', obtain_jwt_token),
    url(r'^auth-jwt-refresh/', refresh_jwt_token),
    url(r'^auth-jwt-verify/', verify_jwt_token),
    url(PREFIX_API + 'password_reset/',
        include('django_rest_passwordreset.urls', namespace='password_reset')),

    path(PREFIX_API, include('sessions.urls')),
    path(PREFIX_API, include('register.urls')),
    path(PREFIX_API, include('devices.urls')),
    path(PREFIX_API, include('clients.urls')),
    path(PREFIX_API, include('profiles.urls')),
    path(PREFIX_API, include('traces.urls')),
    path(PREFIX_API, include('vehicles.urls')),
    path(PREFIX_API, include('vehicles_groups.urls')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
)



