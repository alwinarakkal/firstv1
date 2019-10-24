# Generated by Django 2.2.6 on 2019-10-24 04:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ser', '0017_auto_20191024_0439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='bread',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(15)]),
        ),
        migrations.AlterField(
            model_name='item',
            name='milk',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(15)]),
        ),
        migrations.AlterField(
            model_name='item',
            name='rice',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(15)]),
        ),
        migrations.AlterField(
            model_name='item',
            name='water',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(15)]),
        ),
    ]