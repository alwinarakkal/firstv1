# Generated by Django 2.2.6 on 2019-10-23 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ser', '0014_auto_20191021_0735'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='flat_number',
            new_name='time',
        ),
    ]
