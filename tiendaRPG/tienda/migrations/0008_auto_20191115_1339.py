# Generated by Django 2.2.6 on 2019-11-15 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0007_auto_20191115_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='clase',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.Clase_Personaje'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='derrotas',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='total_puntos',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='victorias',
            field=models.IntegerField(default=0),
        ),
    ]