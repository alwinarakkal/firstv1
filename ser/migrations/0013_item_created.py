# Generated by Django 2.2.5 on 2019-10-08 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ser', '0012_auto_20191008_0833'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
