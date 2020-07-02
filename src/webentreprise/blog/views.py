from django.shortcuts import render
from .models import post 

# Create your views here.
def blog(request):
    return render(request,'blog/blog.html',{'posts':post.objects.all()})