from django.db import models



class Incident(models.Model):
    inc_desc = models.CharField(max_length=50)
    inc_place = models.CharField(max_length=50)
    inc_date = models.CharField(max_length=100)

def __str__(self):
        return self.inc_desc
# Create your models here.
