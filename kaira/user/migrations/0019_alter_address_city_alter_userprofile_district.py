# Generated by Django 4.1.7 on 2023-04-07 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_alter_address_city_alter_userprofile_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(choices=[('Banglore', 'Banglore'), ('Ernakulam', 'Ernakulam'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Madurai', 'Madurai'), ('Hubli', 'Hubli'), ('Kozhikkode', 'Kozhikkode'), ('Kannur', 'Kannur'), ('Hydrabad', 'Hydrabad'), ('Coimbator', 'Coimbator')], max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='district',
            field=models.CharField(blank=True, choices=[('Banglore', 'Banglore'), ('Ernakulam', 'Ernakulam'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Madurai', 'Madurai'), ('Hubli', 'Hubli'), ('Kozhikkode', 'Kozhikkode'), ('Kannur', 'Kannur'), ('Hydrabad', 'Hydrabad'), ('Coimbator', 'Coimbator')], max_length=20, null=True),
        ),
    ]
