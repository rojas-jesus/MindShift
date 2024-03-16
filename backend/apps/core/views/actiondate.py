from django.shortcuts import render
from ..models import ActionDate
from datetime import date, timedelta, datetime

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
    return render(request, "core/actiondate/chart/sad_intensity_today.html", context)


def actiondate_sad_intensity_last_30_days_view(request):
    """
    ActionDate Chart that displays the number of times a sad emotion has been experienced, based in intensity. 
    """
    current_date = datetime.now()
    thirty_days_ago_date = current_date - timedelta(days=30)
    current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    thirty_days_ago_date = thirty_days_ago_date.strftime("%Y-%m-%d %H:%M:%S")

    user = request.user
    last_thirty_days = ActionDate.objects.filter(date_time__range=(thirty_days_ago_date, current_date))

    sad_low = last_thirty_days.filter(user=user,emotion="sad",emotion_intensity="low")
    sad_low_count = sad_low.count()

    sad_medium = last_thirty_days.filter(user=user,emotion="sad",emotion_intensity="medium")
    sad_medium_count = sad_medium.count()

    sad_high = last_thirty_days.filter(user=user,emotion="sad",emotion_intensity="high")
    sad_high_count = sad_high.count()

    sad_very_high = last_thirty_days.filter(user=user,emotion="sad",emotion_intensity="very high")
    sad_very_high_count = sad_very_high.count()

    context = {
        "sad_low_count": sad_low_count ,
        "sad_medium_count": sad_medium_count,
        "sad_high_count": sad_high_count,
        "sad_very_high_count": sad_very_high_count,
    }
    return render(request, "core/actiondate/chart/sad_intensity_last_30_days.html", context)
