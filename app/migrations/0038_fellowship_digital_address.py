# Generated by Django 4.1.3 on 2022-12-19 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0037_zone_affiliated_union'),
    ]

    operations = [
        migrations.AddField(
            model_name='fellowship',
            name='digital_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
