# Generated by Django 2.2.6 on 2019-11-17 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0013_auto_20191115_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesorio',
            name='tipoAccesorio',
            field=models.CharField(choices=[('ca', 'Cascos'), ('pe', 'Petos'), ('ma', 'Manoplas'), ('pa', 'Pantalones'), ('gr', 'Grebas'), ('an', 'Anillos')], max_length=10),
        ),
    ]