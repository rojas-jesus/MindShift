from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy

from .models import Thought, ThoughtDate, Action 
from .forms import ThoughtForm, ThoughtDateForm, ActionForm 

from datetime import timedelta, datetime
from django.db.models import Count

# Thought Views
def home(request):
    return render(request, "core/home.html")


class ThoughtListView(ListView):
    model = Thought
    template_name = "core/thought/list.html"


class ThoughtCreateView(CreateView):
    model = Thought
    form_class = ThoughtForm
    template_name = "core/thought/create.html"
    success_url = reverse_lazy("core:thought-list")


class ThoughtDetailView(DetailView):
    model = Thought
    template_name = "core/thought/detail.html"


class ThoughtUpdateView(UpdateView):
    model = Thought
    form_class = ThoughtForm
    template_name = "core/thought/update.html"
    success_url = reverse_lazy("core:thought-list")


class ThoughtDeleteView(DeleteView):
    model = Thought
    template_name = "core/thought/delete.html"
    success_url = reverse_lazy("core:thought-list")



# ThoughtDate Views
class ThoughtDateListView(ListView):
    model = ThoughtDate
    template_name = "core/thoughtdate/list.html"


class ThoughtDateCreateView(CreateView):
    model = ThoughtDate
    form_class = ThoughtDateForm
    template_name = "core/thoughtdate/create.html"
    success_url = reverse_lazy("core:thought-date-list")  


class ThoughtDateDetailView(DetailView):
    model = ThoughtDate
    template_name = "core/thoughtdate/detail.html"


class ThoughtDateUpdateView(UpdateView):
    model = ThoughtDate
    form_class = ThoughtDateForm
    template_name = "core/thoughtdate/update.html"
    success_url = reverse_lazy("core:thought-date-list")


class ThoughtDateDeleteView(DeleteView):
    model = ThoughtDate
    template_name = "core/thoughtdate/delete.html"
    success_url = reverse_lazy("core:thought-date-list")





def most_relevant_thoughts(request):
    """
    Most relevant thoughts based on the number of occurrences in the last 30 days.
    """
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




# Action Views

class ActionListView(ListView):
    model = Action
    template_name = "core/action/list.html"

    def get_queryset(self):
        return Action.objects.filter(user=self.request.user)


class ActionCreateView(CreateView):
    model = Action
    form_class = ActionForm
    template_name = "core/action/create.html"
    success_url = reverse_lazy("core:action-list")


class ActionDetailView(DetailView):
    model = Action
    template_name = "core/action/detail.html"


class ActionUpdateView(UpdateView):
    model = Action
    form_class = ActionForm
    template_name = "core/action/update.html"
    success_url = reverse_lazy("core:action-list")

class ActionDeleteView(DeleteView):
    model = Action
    template_name = "core/action/delete.html"
    success_url = reverse_lazy("core:action-list")
