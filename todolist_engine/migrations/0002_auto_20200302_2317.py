# Generated by Django 3.0.3 on 2020-03-02 22:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_engine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='add_timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
