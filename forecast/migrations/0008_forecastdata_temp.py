# Generated by Django 5.2.3 on 2025-06-28 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forecast', '0007_alter_forecastdata_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='forecastdata',
            name='temp',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
