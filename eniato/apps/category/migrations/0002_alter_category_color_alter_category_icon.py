# Generated by Django 4.1.1 on 2022-12-11 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='color',
            field=models.CharField(choices=[('blue', 'BLUE'), ('light-blue', 'LIGHT_BLUE'), ('red', 'RED'), ('jigglypuff', 'JIGGLYPUFF'), ('pink', 'PINK'), ('yellow', 'YELLOW'), ('orange', 'ORANGE'), ('green', 'GREEN'), ('purple', 'PURPLE'), ('grey', 'GREY'), ('light-green', 'LIGHT_GREEN'), ('petrel', 'PETREL'), ('primer', 'PRIMER')], max_length=50, verbose_name='Cor da Categoria'),
        ),
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.CharField(choices=[('wallet2', 'WALLET'), ('house', 'HOUSE'), ('cart', 'CART'), ('bookmark-heart', 'BOOKMARK_HEART'), ('calendar-event', 'EVENT'), ('book', 'BOOK'), ('person', 'PERSON'), ('pin-map', 'MAP'), ('car-front', 'CAR'), ('person-video3', 'VIDEO'), ('geo-alt', 'GEO'), ('airplane', 'AIRPLANE'), ('bicycle', 'BICYCLE'), ('umbrella', 'UMBRELLA'), ('graph-up', 'ARROW'), ('justify-left', 'LIST'), ('pie-chart', 'CHART'), ('houses', 'HOUSES'), ('phone', 'PHONE'), ('display', 'DISPLAY'), ('controller', 'CONTROLLER'), ('three-dots', 'THREE_DOTS'), ('shop', 'SHOP'), ('heart', 'HEART'), ('file', 'FILE'), ('cart2', 'CART2'), ('truck', 'TRUNK'), ('star', 'STAR'), ('gift', 'GIFT'), ('minecart', 'MINICART')], max_length=50, verbose_name='Ícone'),
        ),
    ]