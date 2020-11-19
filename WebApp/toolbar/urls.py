from django.urls import path
from toolbar import views

urlpatterns = [
    path('svg',views.svg),
]