# Generated by Django 4.2 on 2023-08-27 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodmenu', '0016_delete_fooddelivery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='detils',
        ),
    ]