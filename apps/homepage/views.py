from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    base = ["about us"]

    return HttpResponse(base)
