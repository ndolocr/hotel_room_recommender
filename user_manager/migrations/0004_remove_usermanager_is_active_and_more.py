# Generated by Django 4.1.5 on 2023-03-25 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_manager', '0003_alter_usermanager_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermanager',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='usermanager',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='usermanager',
            name='supervisor_id',
        ),
    ]