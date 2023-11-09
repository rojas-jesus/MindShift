from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import Thought, ThoughtDate
from .forms import CreateThoughtForm, CreateThoughtDateForm

from datetime import timedelta, datetime
from django.db.models import Count


def Home(request):
    return render(request, "core/home.html")


def ThoughtsList(request):
    thoughts_list = Thought.objects.all()

    context = {"thought_list": thoughts_list}
    return render(request, "core/thoughtslist.html", context)


class CreateThought(CreateView):
    model = Thought
    form_class = CreateThoughtForm
    template_name = "core/createthought.html"
    success_url = reverse_lazy("ThoughtsList")


class CreateThoughtDate(CreateView):
    model = ThoughtDate
    form_class = CreateThoughtDateForm
    template_name = "core/createthoughtdate.html"
    success_url = reverse_lazy("Home")  # TODO: Change the "Home" URL to another appropiate to redirect after a successful operation.


def MostRelevantThoughts(request):
    current_date = datetime.now()
    thirty_days_ago_date = current_date - timedelta(days=30)

    current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    thirty_days_ago_date = thirty_days_ago_date.strftime("%Y-%m-%d %H:%M:%S")

    thoughts_dates_last_thirty_days = ThoughtDate.objects.filter(
        timestamp__range=(thirty_days_ago_date, current_date)
    )
    thoughts_dates_grouped = thoughts_dates_last_thirty_days.values("thought").annotate(
        entries=Count("id")
    )

    context = {
        "thoughts_dates_last_thirty_days": thoughts_dates_last_thirty_days,
        "thoughts_dates_grouped": thoughts_dates_grouped,
    }
    return render(request, "core/mostrelevantthoughts.html", context)
