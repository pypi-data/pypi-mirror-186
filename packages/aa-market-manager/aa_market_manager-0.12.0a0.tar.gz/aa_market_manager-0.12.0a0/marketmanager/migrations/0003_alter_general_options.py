# Generated by Django 3.2.8 on 2021-11-29 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketmanager', '0002_auto_20211129_1339'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='general',
            options={'default_permissions': (), 'managed': False, 'permissions': (('basic_market_browser', 'Can access the Market Browser with standard features'), ('advanced_market_browser', 'Can access the Market Browser with more detail such as the owners of orders'))},
        ),
    ]
