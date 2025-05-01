from django.urls import path
from .views import PredictionAdmission, home

urlpatterns = [
    path('api/predict/', PredictionAdmission.as_view(), name='predict'),
    path('', home)
]
