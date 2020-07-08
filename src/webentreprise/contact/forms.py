from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50, required=True,widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Enter name here'}
    ))
    email = forms.EmailField(label='Email',required=True,widget=forms.EmailInput(
        attrs={'class':'form-control','placeholder':'Enter email'}
    ))
    content = forms.CharField(label='Content', max_length=400, required=True,widget=forms.Textarea(
        attrs={'class':'form-control','rows':3,'placeholder':'Enter comments here'}
    ))