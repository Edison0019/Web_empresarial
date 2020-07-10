from django.shortcuts import render, redirect
from .forms import contactForm
from django.urls import reverse
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    contact_form = contactForm()
    if request.method == 'POST':
        contact_form = contactForm(data=request.POST)
        if contact_form.is_valid(): #if the information is valid then assign the values of the keys to a variables
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            #send email with the confirmation of the contact to the user
            mail = EmailMessage(
                "La cafetiera: New message",
                "From {} <{}>\n\n Wrote \n\n{}".format(name,email,content),
                "no-reply@inbox.mailtrap.io",
                ['edison_0019@hotmail.com'],
                reply_to=[email]
            )
            try:
                mail.send()
                return redirect(reverse('contact')+'?ok')
            except:
               return redirect(reverse('contact')+'?fail') 
            
    return render(request,'contact/contact.html',{'form': contact_form})