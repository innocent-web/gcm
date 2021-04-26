from django.db import models

# Create your models here.


class Compte(models.Model):
    compte = models.CharField(max_length=50, unique=True)
    pcop = models.CharField(max_length=50, unique=True)
    libelle = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return self.compte


class Produit(models.Model):
    ref = models.CharField(max_length=50, unique=True)
    designation = models.CharField(max_length=100)
    unite = models.CharField(max_length=50)
    caracteristique = models.TextField(max_length=255)
    stock = models.IntegerField()
    is_disponible = models.BooleanField(default=True)
    compte = models.ForeignKey(Compte, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.designation