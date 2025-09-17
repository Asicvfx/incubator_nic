from django.urls import path
from . import views

urlpatterns = [
    path("ping/", views.ping),
    path("", views.sum_numbers),
]