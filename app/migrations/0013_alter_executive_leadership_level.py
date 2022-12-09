# Generated by Django 4.1.3 on 2022-12-07 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_union_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executive',
            name='leadership_level',
            field=models.CharField(choices=[('National', 'National'), ('Union', 'Union'), ('Zone', 'Zone'), ('Fellowship', 'Fellowship')], max_length=100),
        ),
    ]
