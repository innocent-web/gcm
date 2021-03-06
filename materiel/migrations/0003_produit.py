# Generated by Django 3.2 on 2021-04-26 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materiel', '0002_alter_compte_libelle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=50, unique=True)),
                ('produit_nom', models.CharField(max_length=100)),
                ('caracteristique', models.TextField(max_length=255)),
                ('stock', models.IntegerField()),
                ('is_disponible', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('compte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materiel.compte')),
            ],
        ),
    ]
