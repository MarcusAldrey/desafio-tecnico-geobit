from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Gender(models.TextChoices):
        MALE = "M"
        FEMALE = "F"

    gender = models.CharField(choices=Gender.choices, max_length=1)

    height = models.IntegerField()
    weight = models.FloatField()
    birthdate = models.DateTimeField()
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    number = IntegerField()

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name or ""}'
