from django.shortcuts import render
from .models import service

# Create your views here.
def services(request):
    serv = service.objects.all()
    context = {
        "elements" : serv
    }
    return render(request,'service/services.html',context)