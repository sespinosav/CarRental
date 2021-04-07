from django.urls import path

from .views import CarRentalView

app_name = "carRental"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('carRental/', CarRentalView.as_view(), name='Car Rental API'),
    path('carRental/<int:pk>', CarRentalView.as_view(), name='Car Rental API'),
]