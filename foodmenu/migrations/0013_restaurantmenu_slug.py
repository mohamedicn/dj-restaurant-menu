# Generated by Django 4.2 on 2023-05-27 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodmenu', '0012_order_alter_bookatable_chooseaddresstable_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantmenu',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
