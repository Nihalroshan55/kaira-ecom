# Generated by Django 4.1.7 on 2023-03-14 08:20

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0002_alter_userprofile_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='district',
            field=models.CharField(blank=True, choices=[('Kannur', 'Kannur'), ('Madurai', 'Madurai'), ('Hydrabad', 'Hydrabad'), ('Hubli', 'Hubli'), ('Banglore', 'Banglore'), ('Ernakulam', 'Ernakulam'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Coimbator', 'Coimbator'), ('Kozhikkode', 'Kozhikkode')], max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100, null=True)),
                ('lastname', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=200)),
                ('address_line_1', models.CharField(max_length=255)),
                ('address_line_2', models.CharField(blank=True, max_length=255)),
                ('phone', models.CharField(max_length=10, null=True, validators=[django.core.validators.RegexValidator(message='Mobile number should only contain digits', regex='^\\d+$')])),
                ('city', models.CharField(choices=[('Kannur', 'Kannur'), ('Madurai', 'Madurai'), ('Hydrabad', 'Hydrabad'), ('Hubli', 'Hubli'), ('Banglore', 'Banglore'), ('Ernakulam', 'Ernakulam'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Coimbator', 'Coimbator'), ('Kozhikkode', 'Kozhikkode')], max_length=255)),
                ('state', models.CharField(choices=[('Kerala', 'Kerala'), ('Tamilnadu', 'Tamilnadu'), ('Karnataka', 'Karnataka'), ('AndraPradesh', 'AndraPradesh')], max_length=255)),
                ('pincode', models.PositiveIntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
