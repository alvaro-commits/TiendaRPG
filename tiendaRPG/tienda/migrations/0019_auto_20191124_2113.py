# Generated by Django 2.2.7 on 2019-11-25 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0018_auto_20191118_2202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enemigo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('vida', models.IntegerField()),
                ('daño', models.FloatField()),
                ('defensa', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='perfil',
            name='daño_total',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='defensa_total',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='vida_total',
            field=models.IntegerField(default=0),
        ),
    ]
