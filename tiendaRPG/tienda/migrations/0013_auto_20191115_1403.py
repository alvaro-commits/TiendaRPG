# Generated by Django 2.2.6 on 2019-11-15 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0012_auto_20191115_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='clase',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.Clase_Personaje'),
        ),
    ]
