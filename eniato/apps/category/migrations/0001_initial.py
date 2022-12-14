# Generated by Django 4.1.1 on 2022-12-07 02:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(blank=True, default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('category_type', models.CharField(choices=[('income', 'INCOME'), ('expense', 'EXPENSE')], max_length=50, verbose_name='Tipo da categoria')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('color', models.CharField(choices=[('blue', 'BLUE'), ('red', 'RED'), ('jigglypuff', 'JIGGLYPUFF'), ('pink', 'PINK'), ('yellow', 'YELLOW'), ('orange', 'ORANGE'), ('green', 'GREEN'), ('purple', 'PURPLE'), ('petrel', 'PETREL'), ('primer', 'PRIMER')], max_length=50, verbose_name='Cor da Categoria')),
                ('icon', models.CharField(choices=[('wallet2', 'WALLET'), ('house', 'HOUSE'), ('cart', 'CART'), ('bookmark-heart', 'HEART'), ('calendar-event', 'EVENT'), ('book', 'BOOK'), ('person', 'PERSON'), ('pin-map', 'MAP'), ('car-front', 'CAR'), ('person-video3', 'VIDEO'), ('bus-front', 'BUS'), ('geo-alt', 'GEO'), ('airplane', 'AIRPLANCE'), ('bicycle', 'BICYCLE'), ('umbrella', 'UMBRELLA'), ('graph-up-arrow', 'ARROW'), ('justify-left', 'LIST'), ('pie-chart', 'CHART'), ('houses', 'HOUSES'), ('phone', 'PHONE')], max_length=50, verbose_name='Ícone')),
                ('default', models.BooleanField(default=False, verbose_name='Padrão do Sistema')),
                ('deleted_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
            managers=[
                ('stored', django.db.models.manager.Manager()),
            ],
        ),
    ]
