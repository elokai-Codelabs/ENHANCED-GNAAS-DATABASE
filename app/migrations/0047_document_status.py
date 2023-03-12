# Generated by Django 4.1.3 on 2023-03-02 00:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0046_remove_fellowship_gender_fellowship_females_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='status',
            field=models.CharField(choices=[('National', 'National'), ('SGUC', 'SGUC'), ('NGUC', 'NGUC')], default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
