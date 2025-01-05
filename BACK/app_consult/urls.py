from django.contrib import admin
from django.urls import path
from app_consult import views
urlpatterns = [
    path('consult/',views.consult)
]
