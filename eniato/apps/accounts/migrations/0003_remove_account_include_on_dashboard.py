# Generated by Django 4.1.1 on 2022-12-17 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_account_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='include_on_dashboard',
        ),
    ]
