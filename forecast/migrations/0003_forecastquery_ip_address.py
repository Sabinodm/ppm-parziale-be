# Generated by Django 5.2.3 on 2025-06-28 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forecast', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='forecastquery',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]
