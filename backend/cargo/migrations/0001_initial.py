# Generated by Django 4.0 on 2023-05-25 17:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)], verbose_name='Вес')),
                ('description', models.TextField(verbose_name='Описание груза')),
                ('delivery_location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='delivery_locations', to='location.location', verbose_name='Место доставки груза')),
                ('pickup_location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pickup_locations', to='location.location', verbose_name='Место получения груза')),
            ],
            options={
                'verbose_name': 'Груз',
                'verbose_name_plural': 'Грузы',
            },
        ),
    ]
