# Generated by Django 2.2.3 on 2019-11-18 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0015_auto_20191117_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='accesorios',
            field=models.ManyToManyField(blank=True, null=True, to='tienda.Perfil_Accesorio'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='recompensa',
            field=models.ManyToManyField(blank=True, null=True, to='tienda.Recompensa'),
        ),
    ]