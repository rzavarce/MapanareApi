from django.urls import path
from vehicles import views

urlpatterns = [
    path('vehicles/', views.VehicleList.as_view()),
    path('vehicles/<int:pk>/', views.VehicleDetail.as_view()),
    path('vehicles/form_data/', views.VehicleAddFormData.as_view()),
    path('vehicles/form_data/<int:pk>/', views.VehicleEditFormData.as_view()),
]
