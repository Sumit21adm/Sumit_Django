# Generated by Django 4.0.3 on 2022-04-01 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj1', '0004_remove_employee_first_name_remove_employee_last_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='bio',
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterModelTable(
            name='employee',
            table='employee',
        ),
    ]