from django.urls import path
from . import views as sv

urlpatterns = [
    #app services
    path('services/', sv.services,name='services'),
]