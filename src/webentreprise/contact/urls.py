from django.urls import path
from . import views as cv

urlpatterns = [
    #app views
    path('contact/', cv.contact,name='contact'),
]