from django.urls import path
from vehicles_groups import views

urlpatterns = [
    path('vehicles_groups/', views.VehiclesGroupList.as_view()),
    path('vehicles_groups/<int:pk>/', views.VehiclesGroupDetail.as_view()),
]
