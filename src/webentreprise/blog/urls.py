from django.urls import path
from . import views as bv

urlpatterns = [
    path('blog/',bv.blog,name='blog')
]