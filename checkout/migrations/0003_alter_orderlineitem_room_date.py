# Generated by Django 3.2.5 on 2021-07-19 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_alter_orderlineitem_room_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='room_date',
            field=models.DateField(),
        ),
    ]