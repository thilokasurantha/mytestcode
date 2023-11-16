from . import views
from django.urls import path

urlpatterns = [
    path('server', views.server, name='server'),
]