from django.urls import path
from . import views as bv

urlpatterns = [
    path('blog/',bv.blog,name='blog'),
    #this code below takes an argument from the user so that
    #the view can interact with the request
    path('blog/category/<int:category_id>/',bv.categor,name='category'),
]