# Generated by Django 4.0.3 on 2022-04-02 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='mobno',
            field=models.IntegerField(default='', max_length=100),
        ),
    ]