from django.shortcuts import render, redirect
from .forms import contactForm
from django.urls import reverse

# Create your views here.
def contact(request):
    contact_form = contactForm()
    if request.method == 'POST':
        contact_form = contactForm(data=request.POST)
        if contact_form.is_valid(): #if the information is valid then assign the values of the keys to a variables
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            return redirect(reverse('contact')+'?ok')
    return render(request,'contact/contact.html',{'form': contact_form})