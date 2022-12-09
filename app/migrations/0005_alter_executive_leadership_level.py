# Generated by Django 4.1.3 on 2022-11-28 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_executive_current_gnaas_fellowship_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executive',
            name='leadership_level',
            field=models.CharField(choices=[('National', 'National'), ('Union', 'Union'), ('Zone', 'Zone'), ('Fellowship', 'Fellowship')], max_length=100),
        ),
    ]
