# Generated by Django 5.1 on 2024-09-07 15:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0003_contests_daily_awards_available'),
        ('extractions', '0003_remove_extractions_winner_extractions_result'),
        ('users', '0002_alter_userawards_award'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userawards',
            name='won_date',
        ),
        migrations.AddField(
            model_name='userawards',
            name='contest',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='UserAwards_Contests', to='contests.contests'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userawards',
            name='extractions',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='UserAwards_Extractions', to='extractions.extractions'),
            preserve_default=False,
        ),
    ]
