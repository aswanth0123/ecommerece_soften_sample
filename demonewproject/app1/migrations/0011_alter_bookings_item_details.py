# Generated by Django 5.0 on 2023-12-29 11:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_alter_bookings_user_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='item_details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.product'),
        ),
    ]