# Generated by Django 5.1 on 2024-08-29 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='awards',
            name='description',
        ),
        migrations.AddField(
            model_name='awards',
            name='code',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='awards',
            name='perday',
            field=models.IntegerField(default=1),
        ),
    ]
