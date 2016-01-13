__author__ = 'ras-al-ghul'

from django import forms

class contactForm(forms.Form):
    name =  forms.CharField(max_length=100,required=True)
    email = forms.EmailField(required=True)
    subject= forms.CharField(max_length=1000,required=False)
    message = forms.CharField(required=True,widget=forms.Textarea)




