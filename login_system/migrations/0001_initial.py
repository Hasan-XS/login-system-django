# Generated by Django 4.2 on 2024-09-10 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40, unique=True)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=65)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
