from django.contrib import admin
from .models import Compte, Produit

# Register your models here.


class CompteAdmin(admin.ModelAdmin):
    list_display = ('compte', 'pcop', 'libelle')


class ProduitAdmin(admin.ModelAdmin):
    list_display = ('ref', 'designation', 'stock', 'compte')


admin.site.register(Compte, CompteAdmin)
admin.site.register(Produit, ProduitAdmin)
