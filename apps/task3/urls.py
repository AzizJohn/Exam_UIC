from django.urls import path

from apps.task3.views import CarDetail

urlpatterns = [
    path('cars/<int:pk>/detail/', CarDetail.as_view(), name='car-detail'),
]