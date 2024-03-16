from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, time

EMOTION_CHOICES = [
    ("sad", "Sad"),
    ("happy", "Happy"),
    ("worry", "Worry"),
    ("angry", "Angry"),
]

INTENSITY = [
    (None, "No Intensity"),
    ("low", "Low"),
    ("medium", "Medium"),
    ("high", "High"),
    ("very high", "Very High"),
]

class Action(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(verbose_name="Description")
    advantages = models.TextField(null=True, blank=True, verbose_name="Advantages")
    disadvantages = models.TextField(null=True, blank=True, verbose_name="Disadvantages")
    facilitator  = models.ManyToManyField("Facilitator", blank=True)
    thought_facilitator = models.ManyToManyField("Thought", blank=True, related_name="facilitator_thought") 
    action_facilitator = models.ManyToManyField("Action", blank=True, related_name="facilitator_action") 
    environment_facilitator = models.ManyToManyField("Environment", blank=True, related_name="facilitator_environment") 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ActionDate(models.Model):
    date = models.DateField(null=True,blank=True)
    time = models.TimeField(null=True, blank=True)
    date_time = models.DateTimeField(null=True, blank=True)
    action = models.ForeignKey("Action", on_delete=models.SET_NULL, null=True, blank=True)
    emotion = models.CharField(
        max_length=20,
        choices=EMOTION_CHOICES,
        null=True,
        blank=True,
        verbose_name="Emotion"
    )
    emotion_intensity = models.CharField(
        max_length=20,
        choices=INTENSITY,
        null=True,
        blank=True,
        verbose_name="Emotion Intensity",
    )
    hour = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    minute = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    second = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    duration_total = models.PositiveBigIntegerField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kargs):
        self.duration_total = (self.hour*3600)+(self.minute*60)+(self.second)

        if self.time:
            self.date_time = datetime.combine(self.date, self.time)
        else:
            self.date_time = datetime.combine(self.date, time())
        super().save(*args, **kargs)

    def __str__(self):
        return f"{self.action} | {self.date} "

class Thought(Action):
    pass

class ThoughtDate(models.Model):
    timestamp = models.DateTimeField(null=True,blank=True, auto_now_add=True)
    thought = models.ForeignKey("Thought", on_delete=models.SET_NULL, null=True, blank=True)
    emotion = models.CharField(
        max_length=20,
        choices=EMOTION_CHOICES,
        null=True,
        blank=True,
        verbose_name="Emotion"
    )
    emotion_intensity = models.CharField(
        max_length=20,
        choices=INTENSITY,
        null=True,
        blank=True,
        verbose_name="Emotion Intensity",
    )
    hour = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    minute = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    second = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    duration_total = models.PositiveBigIntegerField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kargs):
        self.duration_total = (self.hour*3600)+(self.minute*60)+(self.second)
        super().save(*args, **kargs)

    def __str__(self):
        return f"{self.thought} | {self.timestamp.strftime('%d/%m/%Y')}"


class Facilitator(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(verbose_name="Description")

    def __str__(self):
        return self.name

class Environment(Facilitator):
    pass

