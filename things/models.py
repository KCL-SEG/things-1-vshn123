from django.db import models

# Create your models here.
class Thing(models.Model):
    self.name = models.CharField()
    self.description = models.TextField()
    self.quantity = models.IntegerField()