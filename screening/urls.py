from django.urls import path
from screening import views

urlpatterns = [
    path('', views.screening, name="screening")
]
