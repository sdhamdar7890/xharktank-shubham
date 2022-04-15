from django.db import models


# Create your models here.
class Pitches(models.Model):
    entrepreneur = models.CharField(max_length=248, blank=False)
    pitchTitle = models.TextField(blank=False)
    pitchIdea = models.TextField(blank=False)
    askAmount = models.DecimalField(max_digits=124, decimal_places=4, blank=False)
    equity = models.DecimalField(max_digits=10, decimal_places=7, blank=False)


class Object(models.Model):
    investor = models.TextField(max_length=248, blank=False)
    amount = models.DecimalField(max_digits=20, decimal_places=4, blank=False)
    equity = models.DecimalField(max_digits=10, decimal_places=7, blank=False)
    comment = models.CharField(max_length=500)
    pitches = models.ForeignKey('Pitches', on_delete=models.CASCADE, blank=False)
