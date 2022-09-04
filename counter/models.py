from django.db import models

# Create your models here.
class CounterModel(models.Model):
    press_count = models.IntegerField(null=True, default=0)