# Generated by Django 4.1.1 on 2022-12-20 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0011_remove_transaction_file_remove_transaction_ignore'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='store',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='tag',
        ),
    ]
