# Generated by Django 4.2 on 2024-09-10 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_system', '0002_user_groups_user_is_active_user_is_staff_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
    ]
