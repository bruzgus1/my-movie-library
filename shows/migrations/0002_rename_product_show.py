# Generated by Django 3.2 on 2023-08-15 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Show',
        ),
    ]
