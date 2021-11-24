from django.urls import path
from . import views

urlpatterns = [
    path('', views.distance_calculation_view, name='distance_view'),
]