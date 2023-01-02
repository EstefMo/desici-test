import os

from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=120)
    picture = models.TextField(max_length=100)
    birth_date = models.DateField()


class Address(models.Model):
    street_name = models.CharField(max_length=255)
    external_number = models.CharField(max_length=10)
    internal_number = models.CharField(max_length=10)
    settlement = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=3)
    references = models.CharField(max_length=255)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


class Phone(models.Model):
    type = models.IntegerField()
    alias = models.CharField(max_length=255)
    number = models.CharField(max_length=50)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
