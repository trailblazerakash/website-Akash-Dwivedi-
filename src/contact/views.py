from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import contactForm

# Create your views here.
def contact(request):
    form = contactForm(request.POST or None)
    context = {'form':form}
    if form.is_valid():

        name = form.cleaned_data['name']
        message = form.cleaned_data['message']
        subject =form.cleaned_data['subject']
        emailfrom = form.cleaned_data['email']
        emailto = ["akash.teehnoge@gmail.com"]
        message = message + "\n\n\n from:" + emailfrom
        send_mail(subject,message,emailfrom,emailto,fail_silently=False)







        form =  contactForm(None)
       # Render the form with error messages (if any).
    return render(request, 'contact.html', context)




