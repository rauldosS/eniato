# Generated by Django 4.1.1 on 2022-12-11 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_transaction_daily_balance_alter_store_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='daily_balance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='daily_balance_transaction', to='transaction.dailybalance'),
        ),
    ]
