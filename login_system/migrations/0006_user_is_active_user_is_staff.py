# Generated by Django 4.2 on 2024-09-10 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_system', '0005_remove_user_is_active_remove_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
