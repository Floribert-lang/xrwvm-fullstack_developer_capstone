from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# Car Make Model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}"

# Car Model
class CarModel(models.Model):
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    HATCHBACK = 'Hatchback'
    CONVERTIBLE = 'Convertible'

    CAR_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (HATCHBACK, 'Hatchback'),
        (CONVERTIBLE, 'Convertible'),
    ]

    make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='models')
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=CAR_TYPES, default=SEDAN)
    year = models.IntegerField(validators=[MinValueValidator(2015), MaxValueValidator(2023)])
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.make.name} {self.name} ({self.year})"
