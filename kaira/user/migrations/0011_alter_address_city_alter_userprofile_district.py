# Generated by Django 4.1.7 on 2023-03-24 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_rename_size_size_size_alter_address_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(choices=[('Banglore', 'Banglore'), ('Coimbator', 'Coimbator'), ('Hydrabad', 'Hydrabad'), ('Kannur', 'Kannur'), ('Madurai', 'Madurai'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Ernakulam', 'Ernakulam'), ('Hubli', 'Hubli'), ('Kozhikkode', 'Kozhikkode')], max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='district',
            field=models.CharField(blank=True, choices=[('Banglore', 'Banglore'), ('Coimbator', 'Coimbator'), ('Hydrabad', 'Hydrabad'), ('Kannur', 'Kannur'), ('Madurai', 'Madurai'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Ernakulam', 'Ernakulam'), ('Hubli', 'Hubli'), ('Kozhikkode', 'Kozhikkode')], max_length=20, null=True),
        ),
    ]