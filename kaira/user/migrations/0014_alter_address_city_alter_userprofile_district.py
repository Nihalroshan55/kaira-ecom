# Generated by Django 4.1.7 on 2023-03-24 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_alter_address_city_alter_userprofile_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(choices=[('Ernakulam', 'Ernakulam'), ('Coimbator', 'Coimbator'), ('Banglore', 'Banglore'), ('Hubli', 'Hubli'), ('Hydrabad', 'Hydrabad'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Madurai', 'Madurai'), ('Kannur', 'Kannur'), ('Kozhikkode', 'Kozhikkode')], max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='district',
            field=models.CharField(blank=True, choices=[('Ernakulam', 'Ernakulam'), ('Coimbator', 'Coimbator'), ('Banglore', 'Banglore'), ('Hubli', 'Hubli'), ('Hydrabad', 'Hydrabad'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Madurai', 'Madurai'), ('Kannur', 'Kannur'), ('Kozhikkode', 'Kozhikkode')], max_length=20, null=True),
        ),
    ]