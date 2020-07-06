from django.shortcuts import render, get_object_or_404
from .models import page

# Create your views here.
def pages(request,page_id):
    page_list = get_object_or_404(page,id=page_id)
    return render(request,'pages/sample.html',{'pages': page_list})