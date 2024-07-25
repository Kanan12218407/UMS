# Generated by Django 5.0.7 on 2024-07-25 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home1', '0008_scholarship'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counselling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('preferred_timeslot', models.CharField(choices=[('morning', 'Morning'), ('afternoon', 'Afternoon'), ('evening', 'Evening')], max_length=20)),
            ],
        ),
    ]
