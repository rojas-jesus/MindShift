from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied

from .models import Thought, ThoughtDate, Action, ActionDate
from .forms import ThoughtForm, ThoughtDateForm, ActionForm 

from datetime import date, timedelta, datetime
from django.db.models import Count

# Thought Views
def home(request):
    return render(request, "core/home.html")


class ThoughtListView(ListView):
    model = Thought
    template_name = "core/thought/list.html"
    
    def get_queryset(self):
        return Thought.objects.filter(user=self.request.user)


class ThoughtCreateView(CreateView):
    model = Thought
    form_class = ThoughtForm
    template_name = "core/thought/create.html"
    success_url = reverse_lazy("core:thought-list")

    def form_valid(self, form):
        """Auto-assign current user to 'user' field of Thought form"""
        form.instance.user = self.request.user
        return super().form_valid(form)


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

    def get_queryset(self):
        return ThoughtDate.objects.filter(user=self.request.user)

class ThoughtDateCreateView(CreateView):
    model = ThoughtDate
    form_class = ThoughtDateForm
    template_name = "core/thoughtdate/form.html"
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





def most_relevant_thoughts_view(request):
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

    def form_valid(self, form):
        """Auto-assign current user to 'user' field of Action form"""
        form.instance.user = self.request.user
        return super().form_valid(form)


class ActionDetailView(DetailView):
    model = Action
    template_name = "core/action/detail.html"

    def dispatch(self, request, *args, **kwargs):
        """
        If the user associated with the object is different from the current
        user, a PermissionDenied exception is raised.
        """
        obj = self.get_object()
        if obj.user != self.request.user:
            raise PermissionDenied() 
        return super().dispatch(request, *args, **kwargs)


class ActionUpdateView(UpdateView):
    model = Action
    form_class = ActionForm
    template_name = "core/action/update.html"
    success_url = reverse_lazy("core:action-list")

    def dispatch(self, request, *args, **kwargs):
        """
        If the user associated with the object is different from the current
        user, a PermissionDenied exception is raised.
        """
        obj = self.get_object()
        if obj.user != self.request.user:
            raise PermissionDenied() 
        return super().dispatch(request, *args, **kwargs)


class ActionDeleteView(DeleteView):
    model = Action
    template_name = "core/action/delete.html"
    success_url = reverse_lazy("core:action-list")

    def dispatch(self, request, *args, **kwargs):
        """
        If the user associated with the object is different from the current
        user, a PermissionDenied exception is raised.
        """
        obj = self.get_object()
        if obj.user != self.request.user:
            raise PermissionDenied() 
        return super().dispatch(request, *args, **kwargs)

# Action Views Extra

def action_emotion_chart_view(request):
    """
    Chart that displays the number of times a type of emotion has been experienced, based on all actions
    """
    user = request.user

    action_emotion_sad = Action.objects.filter(user=user,emotion=("sad"))
    action_emotion_sad = action_emotion_sad.count()

    action_emotion_worry = Action.objects.filter(user=user,emotion=("worry"))
    action_emotion_worry = action_emotion_worry.count()

    action_emotion_happy = Action.objects.filter(user=user,emotion=("happy"))
    action_emotion_happy = action_emotion_happy.count()

    action_emotion_angry = Action.objects.filter(user=user,emotion=("angry"))
    action_emotion_angry = action_emotion_angry.count()

    context = {
        "action_emotion_sad": action_emotion_sad,
        "action_emotion_worry": action_emotion_sad,
        "action_emotion_happy": action_emotion_happy,
        "action_emotion_angry": action_emotion_angry,
    }
    return render(request, "core/action/emotionchart.html", context)



def actiondate_sad_intensity_chart_view(request):
    """
    ActionDate Chart that displays the number of times a sad emotion has been experienced, based in intensity. 
    """
    current_date = datetime.now()
    thirty_days_ago_date = current_date - timedelta(days=30)
    current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    thirty_days_ago_date = thirty_days_ago_date.strftime("%Y-%m-%d %H:%M:%S")

    user = request.user
    last_thirty_days = ActionDate.objects.filter(date_time__range=(thirty_days_ago_date, current_date))

    last_thirty_days_sad_low = last_thirty_days.filter(user=user,emotion="sad",emotion_intensity="low")
    last_thirty_days_sad_low = last_thirty_days_sad_low.count()

    last_thirty_days_sad_medium = last_thirty_days.filter(user=user,emotion="sad",emotion_intensity="medium")
    last_thirty_days_sad_medium = last_thirty_days_sad_medium.count()

    last_thirty_days_sad_high = last_thirty_days.filter(user=user,emotion="sad",emotion_intensity="high")
    last_thirty_days_sad_high = last_thirty_days_sad_high.count()

    last_thirty_days_sad_very_high = last_thirty_days.filter(user=user,emotion="sad",emotion_intensity="very high")
    last_thirty_days_sad_very_high = last_thirty_days_sad_very_high.count()

    context = {
        "last_thirty_days_sad_low": last_thirty_days_sad_low,
        "last_thirty_days_sad_medium": last_thirty_days_sad_medium,
        "last_thirty_days_sad_high": last_thirty_days_sad_high,
        "last_thirty_days_sad_very_high": last_thirty_days_sad_very_high,
    }
    return render(request, "core/actiondate/chart_sad_intensity.html", context)


def actiondate_today_sad_intensity_chart_view(request):
    """
    ActionDate Chart that displays the number of times a sad emotion has been experienced, categorized by intensity, for the current user date.
    """
    user = request.user
    today_date = date.today()
    today_date_time = today_date.strftime("%Y-%m-%d %H:%M:%S")
    today = ActionDate.objects.filter(date_time__gte=today_date_time)

    today_sad_low = today.filter(user=user,emotion="sad",emotion_intensity="low").count()
    today_sad_medium = today.filter(user=user,emotion="sad",emotion_intensity="medium").count()
    today_sad_high = today.filter(user=user,emotion="sad",emotion_intensity="high").count()
    today_sad_very_high = today.filter(user=user,emotion="sad",emotion_intensity="very high").count()

    context = {
        "today_sad_low": today_sad_low,
        "today_sad_medium": today_sad_medium,
        "today_sad_high": today_sad_high,
        "today_sad_very_high": today_sad_very_high,
    }
    return render(request, "core/actiondate/chart_today_sad_intensity.html", context)

