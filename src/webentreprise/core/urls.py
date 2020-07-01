from django.urls import path
from . import views as cv

urlpatterns = [
    #app views
    path('', cv.home,name='home'),
    path('about/', cv.about,name='about'),
    path('store/', cv.visit_us,name='store'),
    path('contact/', cv.contact,name='contact'),
    path('blog/', cv.blog,name='blog'),
    path('sample/', cv.sample,name='sample'),
]