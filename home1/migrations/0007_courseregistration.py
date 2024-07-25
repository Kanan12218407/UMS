# Generated by Django 5.0.7 on 2024-07-25 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home1', '0006_contact_date_alter_contact_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courseregistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('father_name', models.CharField(max_length=100)),
                ('mother_name', models.CharField(max_length=100)),
                ('father_occupation', models.CharField(max_length=100)),
                ('mother_occupation', models.CharField(max_length=100)),
                ('academic_details', models.TextField()),
                ('course', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
