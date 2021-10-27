from django.db import models

# Create your models here.
class Unemployment(models.Model):
    geoid = models.CharField(max_length=50)
    county = models.CharField(max_length=100)
    year = models.IntegerField()
    labor_force = models.IntegerField()
    value = models.PositiveIntegerField()
    rate = models.FloatField()

    def __str__(self):
        return self.geoid, self.county, self.year, self.rate