from django.db import models

class Thought(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    advantages = models.TextField(null = True, blank = True)
    disadvantages = models.TextField(null = True, blank = True)

class State(models.Model):
    date = models.DateTimeField()
    duration = models.PositiveSmallIntegerField()
    thought = models.ForeignKey(Thought, on_delete=models.SET_NULL, null=True)
