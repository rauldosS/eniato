# Generated by Django 4.1.1 on 2022-12-21 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objective', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='objective',
            name='description',
        ),
    ]
