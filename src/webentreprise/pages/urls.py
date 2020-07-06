from django.urls import path
from . import views as pv

urlpatterns = [
    #app services
    path('page/<int:page_id>/', pv.pages,name='pages'),
]