# Generated by Django 2.2.6 on 2019-11-17 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0014_auto_20191117_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='accesorio',
            name='tier',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='accesorio',
            name='tipoAccesorio',
            field=models.CharField(choices=[('ca', 'Casco'), ('pe', 'Peto'), ('ma', 'Manoplas'), ('pa', 'Pantalones'), ('gr', 'Grebas'), ('an', 'Anillo')], max_length=10),
        ),
    ]