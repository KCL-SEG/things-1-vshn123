from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True, validators=[RegexValidator(r'^.+$')])
    description = models.TextField(max_length=120)
    quantity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])