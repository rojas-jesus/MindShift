from django.db import models

EMOTION_CHOICES = [
    ("sad", "Sad"),
    ("happy", "Happy"),
    ("worry", "Worry"),
    ("angry", "Angry"),
]


class Thought(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    advantages = models.TextField(null=True, blank=True)
    disadvantages = models.TextField(null=True, blank=True)
    emotion = models.CharField(
        max_length=20, choices=EMOTION_CHOICES, null=True, blank=True
    )


class ThoughtDate(models.Model):
    timestamp = models.DateTimeField()
    duration = models.PositiveSmallIntegerField()
    thought = models.ForeignKey(Thought, on_delete=models.SET_NULL, null=True)


# class State(models.Model):
#    date = models.DateTimeField()
#    duration = models.PositiveSmallIntegerField()
#    thought = models.ForeignKey(Thought, on_delete=models.SET_NULL, null=True)
