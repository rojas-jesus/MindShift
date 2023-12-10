from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    base = ["about us"]

    return HttpResponse(base)

def about_us(request):
    text = ["link"]

    return HttpResponse(text)
