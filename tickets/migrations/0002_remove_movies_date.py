# Generated by Django 4.2.5 on 2023-09-28 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='date',
        ),
    ]