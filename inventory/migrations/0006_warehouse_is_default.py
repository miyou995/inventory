# Generated by Django 4.0.3 on 2022-03-23 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_remove_warehouse_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouse',
            name='is_default',
            field=models.BooleanField(default=False, verbose_name='Dépot principale'),
        ),
    ]