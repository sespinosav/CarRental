from django.urls import path

from .views import CarView

app_name = "cars"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('cars/', CarView.as_view(), name='API RENTAL CARS'),
    path('cars/<int:pk>', CarView.as_view(), name='API RENTAL CARS'),
]