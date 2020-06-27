from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('home')

def about(request):
    return HttpResponse('History')

def services(request):
    return HttpResponse('services')

def visit_us(request):
    return HttpResponse('visitanos')

def contact(request):
    return HttpResponse('Contact us')

def blog(request):
    return HttpResponse('Blog')

def sample(request):
    return HttpResponse('sample')