from django.urls import path
from . import views

urlpatterns = [
    path("ping/", views.ping, name="ping"),
    path("sum/", views.sum_numbers, name="sum_numbers"),
]
