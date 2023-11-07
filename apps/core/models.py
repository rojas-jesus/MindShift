from django.db import models

EMOTION_CHOICES = [
    ("sad", "Sad"),
    ("happy", "Happy"),
    ("worry", "Worry"),
    ("angry", "Angry"),
]

EMOTION_INTENSITY = [
    (None, "No Intensity"),
    ("low", "Low"),
    ("medium", "Medium"),
    ("high", "High"),
    ("severe", "severe"),
]

THOUGHT_INTENSITY = [
    (None, "No Intensity"),
    ("low", "Low"),
    ("medium", "Medium"),
    ("high", "High"),
    ("severe", "Severe"),
]


class Thought(models.Model):
    name = models.CharField(max_length=150)
    thought_intensity = models.CharField(
        max_length=20,
        choices=THOUGHT_INTENSITY, 
        null=True, 
        blank=True,
        verbose_name="Thought Intensity",
    )
    description = models.TextField()
    advantages = models.TextField(null=True, blank=True)
    disadvantages = models.TextField(null=True, blank=True)
    emotion = models.CharField(max_length=20,choices=EMOTION_CHOICES, null=True, blank=True)
    emotion_intensity = models.CharField(
        max_length=20,
        choices=EMOTION_INTENSITY,
        null=True,
        blank=True,
        verbose_name="Emotion Intensity",
    )


class ThoughtDate(models.Model):
    timestamp = models.DateTimeField()
    duration = models.PositiveSmallIntegerField()
    thought = models.ForeignKey(Thought, on_delete=models.SET_NULL, null=True)


# class State(models.Model):
#    date = models.DateTimeField()
#    duration = models.PositiveSmallIntegerField()
#    thought = models.ForeignKey(Thought, on_delete=models.SET_NULL, null=True)
