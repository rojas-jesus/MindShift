from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy 

from .models import Thought, ThoughtDate 
from .forms import CreateThoughtForm, CreateThoughtDateForm

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

class CreateThoughtDate(CreateView):
    model = ThoughtDate
    form_class = CreateThoughtDateForm 
    template_name = "createthoughtdate.html"
    success_url = reverse_lazy("Home") # TODO: Change the "Home" URL to another appropiate to redirect after a successful operation.


