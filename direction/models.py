from django.db import models


# Create your models here.


class Direction(models.Model):
    abreviation = models.CharField(max_length=50, unique=True)
    alias = models.SlugField(max_length=100, unique=True)
    parent = models.CharField(max_length=100, blank=True)
    direction_nom = models.TextField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'direction'
        verbose_name_plural = 'directions'

    def __str__(self):
        return self.abreviation


class Service(models.Model):
    abreviation = models.CharField(max_length=50, unique=True)
    alias = models.SlugField(max_length=100, unique=True)
    service_nom = models.TextField(max_length=255, blank=True)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'service'
        verbose_name_plural = 'services'

    def __str__(self):
        return self.abreviation
