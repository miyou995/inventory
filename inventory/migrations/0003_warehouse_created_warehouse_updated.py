# Generated by Django 4.0.3 on 2022-03-20 10:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_rename_quantite_warehouseitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouse',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date de Création'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='warehouse',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Date de dernière mise à jour'),
        ),
    ]
