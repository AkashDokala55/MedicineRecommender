from django.db import models

class Medicine(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.TextField()
    dosage = models.CharField(max_length=200)
    side_effects = models.TextField()

def __str__(self):
     return self.name
