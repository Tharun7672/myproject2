from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# Create your views here.
def index(request):

    dests= Destination.objects.all()


    return render(request, "index.html", {'dests': dests})
def tours(request):
    dests= Destination.objects.all()


    return render(request, "tours.html", {'dests': dests})
def about(request):
    return render(request, "about.html")
def register(request):
    return render(request, "regiter.html")
def login(request):
    return render(request, "login.html")