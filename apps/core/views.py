from django.shortcuts import render
from .models import Thought 

def Home(request):
    return render(request,"home.html")


def ThoughtsList(request):
    thoughts_list = Thought.objects.all()

    context = {
            "thought_list" : thoughts_list
    }
    return render(request, "thoughtslist.html", context)

