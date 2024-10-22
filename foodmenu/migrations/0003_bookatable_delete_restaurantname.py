# Generated by Django 4.2 on 2023-05-03 22:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('foodmenu', '0002_restaurantname'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookATable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ChooseTableSize', models.IntegerField(default=2, max_length=3)),
                ('ChooseADay', models.DateField(default=django.utils.timezone.now)),
                ('ChooseATime', models.TimeField(default=django.utils.timezone.now)),
                ('ChooseAddressTable', models.IntegerField(default=1, max_length=2)),
                ('NotesIfAny', models.TextField(blank=True, max_length=200, null=True)),
                ('IsTableActive', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='RestaurantName',
        ),
    ]
