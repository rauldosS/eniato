# Generated by Django 4.1.1 on 2022-12-21 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0013_remove_store_deleted_by_remove_store_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='installment',
        ),
    ]
