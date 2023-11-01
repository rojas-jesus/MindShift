from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy 

from .models import Thought 
from .forms import CreateThoughtForm

def Home(request):

    return render(request,"home.html")


def ThoughtsList(request):
    thoughts_list = Thought.objects.all()

    context = {
            "thought_list" : thoughts_list
    }
    return render(request, "thoughtslist.html", context)


class CreateThought(CreateView):
    model = Thought
    form_class = CreateThoughtForm 
    template_name = "createthought.html"
    success_url = reverse_lazy("ThoughtsList")

