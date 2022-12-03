from . import views
from django.urls import path

urlpatterns = [
    path("app", views.app, name="app"),
    path('app/call', views.call, name="call")
]