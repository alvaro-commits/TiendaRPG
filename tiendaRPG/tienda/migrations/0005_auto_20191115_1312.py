# Generated by Django 2.2.6 on 2019-11-15 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0004_auto_20191114_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carro',
            name='items',
        ),
        migrations.AddField(
            model_name='carro',
            name='items',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='tienda.CarroProducto'),
            preserve_default=False,
        ),
    ]