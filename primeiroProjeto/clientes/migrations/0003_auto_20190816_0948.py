# Generated by Django 2.2.4 on 2019-08-16 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20190816_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='salary',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
