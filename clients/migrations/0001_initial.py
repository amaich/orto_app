# Generated by Django 5.0.4 on 2024-05-01 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('birthdate', models.IntegerField()),
                ('email', models.CharField(max_length=150)),
                ('phonenumber', models.CharField(max_length=20)),
            ],
        ),
    ]
