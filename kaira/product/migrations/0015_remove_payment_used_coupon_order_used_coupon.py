# Generated by Django 4.1.7 on 2023-04-12 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_payment_used_coupon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='used_coupon',
        ),
        migrations.AddField(
            model_name='order',
            name='used_coupon',
            field=models.CharField(blank=True, default='empty', max_length=100),
        ),
    ]