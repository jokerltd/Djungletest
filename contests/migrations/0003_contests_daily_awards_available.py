# Generated by Django 5.1 on 2024-09-05 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0002_contests_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='contests',
            name='daily_awards_available',
            field=models.IntegerField(default=24),
        ),
    ]