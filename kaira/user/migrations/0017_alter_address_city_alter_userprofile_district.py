# Generated by Django 4.1.7 on 2023-03-27 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_address_is_default_alter_address_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(choices=[('Kannur', 'Kannur'), ('Banglore', 'Banglore'), ('Hydrabad', 'Hydrabad'), ('Ernakulam', 'Ernakulam'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Hubli', 'Hubli'), ('Madurai', 'Madurai'), ('Kozhikkode', 'Kozhikkode'), ('Coimbator', 'Coimbator')], max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='district',
            field=models.CharField(blank=True, choices=[('Kannur', 'Kannur'), ('Banglore', 'Banglore'), ('Hydrabad', 'Hydrabad'), ('Ernakulam', 'Ernakulam'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Hubli', 'Hubli'), ('Madurai', 'Madurai'), ('Kozhikkode', 'Kozhikkode'), ('Coimbator', 'Coimbator')], max_length=20, null=True),
        ),
    ]