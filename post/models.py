from django.db import models

# Create your models here.
class Post(models.Model):
    index = models.DecimalField(max_digits=8,
        decimal_places=2,
        default=0.0,
        blank=True)
    strategy = models.DecimalField(max_digits=8,
        decimal_places=2,
        default=0.0,
        blank=True)
    process = models.DecimalField(max_digits=8,
        decimal_places=2,
        default=0.0,
        blank=True)
    people = models.DecimalField(max_digits=8,
        decimal_places=2,
        default=0.0,
        blank=True)
    customers = models.DecimalField(max_digits=8,
        decimal_places=2,
        default=0.0,
        blank=True)
