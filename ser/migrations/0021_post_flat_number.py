# Generated by Django 2.2.6 on 2019-10-28 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ser', '0020_auto_20191028_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='flat_number',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
