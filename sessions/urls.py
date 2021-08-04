from django.urls import path
from sessions import views

urlpatterns = [
    path('session/', views.SessionViewSet.as_view({'get': 'list'})),
]
