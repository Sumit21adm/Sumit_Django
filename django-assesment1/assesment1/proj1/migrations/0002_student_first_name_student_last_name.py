# Generated by Django 4.0.3 on 2022-03-31 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]