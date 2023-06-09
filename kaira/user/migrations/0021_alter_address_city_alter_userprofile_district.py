# Generated by Django 4.1.7 on 2023-04-10 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_alter_address_city_alter_productvarient_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(choices=[('Hubli', 'Hubli'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Banglore', 'Banglore'), ('Coimbator', 'Coimbator'), ('Madurai', 'Madurai'), ('Kannur', 'Kannur'), ('Hydrabad', 'Hydrabad'), ('Kozhikkode', 'Kozhikkode'), ('Ernakulam', 'Ernakulam')], max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='district',
            field=models.CharField(blank=True, choices=[('Hubli', 'Hubli'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Banglore', 'Banglore'), ('Coimbator', 'Coimbator'), ('Madurai', 'Madurai'), ('Kannur', 'Kannur'), ('Hydrabad', 'Hydrabad'), ('Kozhikkode', 'Kozhikkode'), ('Ernakulam', 'Ernakulam')], max_length=20, null=True),
        ),
    ]
