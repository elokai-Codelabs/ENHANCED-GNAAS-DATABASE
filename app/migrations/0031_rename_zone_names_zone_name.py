# Generated by Django 4.1.3 on 2022-12-11 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_zone_names_alter_position_position'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Zone_Names',
            new_name='Zone_Name',
        ),
    ]
