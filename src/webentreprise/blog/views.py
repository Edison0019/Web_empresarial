from django.shortcuts import render, get_list_or_404
from .models import post,category

# Create your views here.
def blog(request):
    return render(request,'blog/blog.html',{'posts':post.objects.all()})

def categor(request,category_id):
    cat = category.objects.get(id=category_id)
    return render(request,'blog/category.html',{'category' : cat})
