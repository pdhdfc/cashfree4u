from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about-us.html')

def services(request):
    return render(request, 'services.html')

def help_center_category(request):
    return render(request, 'help-center-category.html')

def help_center(request):
    return render(request, 'help-center.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')