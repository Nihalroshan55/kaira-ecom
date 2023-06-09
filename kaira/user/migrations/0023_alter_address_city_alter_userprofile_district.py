# Generated by Django 4.1.7 on 2023-04-12 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_alter_address_city_alter_userprofile_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(choices=[('Madurai', 'Madurai'), ('Kozhikkode', 'Kozhikkode'), ('Kannur', 'Kannur'), ('Banglore', 'Banglore'), ('Hubli', 'Hubli'), ('Ernakulam', 'Ernakulam'), ('Coimbator', 'Coimbator'), ('Hydrabad', 'Hydrabad'), ('Thiruvananthapuram', 'Thiruvananthapuram')], max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='district',
            field=models.CharField(blank=True, choices=[('Madurai', 'Madurai'), ('Kozhikkode', 'Kozhikkode'), ('Kannur', 'Kannur'), ('Banglore', 'Banglore'), ('Hubli', 'Hubli'), ('Ernakulam', 'Ernakulam'), ('Coimbator', 'Coimbator'), ('Hydrabad', 'Hydrabad'), ('Thiruvananthapuram', 'Thiruvananthapuram')], max_length=20, null=True),
        ),
    ]
