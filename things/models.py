from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True, validator=[RegexValidator(regex=r'^.+$')])
    description = models.TextField(max_length=120)
    quantity = models.IntegerField(validator=[MinValueValidator(limit_value=0), MaxValueValidator(limit_value=100)])