# Generated by Django 4.2 on 2023-05-04 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodmenu', '0003_bookatable_delete_restaurantname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookatable',
            name='ChooseAddressTable',
            field=models.CharField(default=1, max_length=2),
        ),
    ]
