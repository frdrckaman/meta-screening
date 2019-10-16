from django.urls import path, include
from screening import views

urlpatterns = [
    path('', views.screening, name="screening")
]