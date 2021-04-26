# Generated by Django 3.2 on 2021-04-26 07:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('materiel', '0003_produit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produit',
            old_name='produit_nom',
            new_name='designation',
        ),
        migrations.AddField(
            model_name='produit',
            name='unite',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
