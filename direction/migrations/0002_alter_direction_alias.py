# Generated by Django 3.2 on 2021-04-26 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('direction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direction',
            name='alias',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]