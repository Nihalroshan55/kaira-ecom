# Generated by Django 4.1.7 on 2023-03-24 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_cartitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='size',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
