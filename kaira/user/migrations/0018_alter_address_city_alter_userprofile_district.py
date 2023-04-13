# Generated by Django 4.1.7 on 2023-04-05 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_alter_address_city_alter_userprofile_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(choices=[('Hubli', 'Hubli'), ('Kannur', 'Kannur'), ('Banglore', 'Banglore'), ('Madurai', 'Madurai'), ('Coimbator', 'Coimbator'), ('Kozhikkode', 'Kozhikkode'), ('Hydrabad', 'Hydrabad'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Ernakulam', 'Ernakulam')], max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='district',
            field=models.CharField(blank=True, choices=[('Hubli', 'Hubli'), ('Kannur', 'Kannur'), ('Banglore', 'Banglore'), ('Madurai', 'Madurai'), ('Coimbator', 'Coimbator'), ('Kozhikkode', 'Kozhikkode'), ('Hydrabad', 'Hydrabad'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Ernakulam', 'Ernakulam')], max_length=20, null=True),
        ),
    ]