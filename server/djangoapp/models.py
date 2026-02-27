from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country = models.CharField(max_length=100, default="USA")

    def __str__(self):
        return self.name


class CarModel(models.Model):
    SEDAN = "Sedan"
    SUV = "SUV"
    WAGON = "Wagon"
    COUPE = "Coupe"
    CONVERTIBLE = "Convertible"
    HATCHBACK = "Hatchback"
    TRUCK = "Truck"

    CAR_TYPES = [
        (SEDAN, "Sedan"),
        (SUV, "SUV"),
        (WAGON, "Wagon"),
        (COUPE, "Coupe"),
        (CONVERTIBLE, "Convertible"),
        (HATCHBACK, "Hatchback"),
        (TRUCK, "Truck"),
    ]

    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField()
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=CAR_TYPES, default=SEDAN)
    year = models.IntegerField(
        validators=[MinValueValidator(2015), MaxValueValidator(2023)],
        default=2023,
    )

    def __str__(self):
        return f"{self.car_make.name} {self.name}"
