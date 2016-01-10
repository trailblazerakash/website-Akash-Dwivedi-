from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request ,'home.html')
def about(request):
    return render(request ,'about.html')
def career(request):
    return render(request ,'service.html')
def gallery(request):
    return render(request ,'gallery.html')
def contact(request):
    return render(request ,'contact.html')
def Page_Not_Found(request):
    return render(request ,'404.html')
