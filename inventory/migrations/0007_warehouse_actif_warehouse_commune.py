# Generated by Django 4.0.3 on 2022-03-23 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
        ('inventory', '0006_warehouse_is_default'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouse',
            name='actif',
            field=models.BooleanField(default=True, verbose_name='actif'),
        ),
        migrations.AddField(
            model_name='warehouse',
            name='commune',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='location.commune'),
        ),
    ]
