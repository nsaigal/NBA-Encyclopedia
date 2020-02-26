from django.db import models

# Create your models here.
class Player(models.Model):
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    position = models.CharField(max_length=10, blank=True, null=True)
    height = models.IntegerField("Height (in)")
    weight = models.IntegerField("Weight (lb)")
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    college = models.CharField(max_length=50, blank=True, null=True)