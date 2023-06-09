# Generated by Django 4.2.2 on 2023-06-17 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GroundZero', '0003_alter_vistaobra_imgvista_alter_vistaobra_nombrev'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreAr', models.CharField(max_length=50)),
                ('apellidoAr', models.CharField(blank=True, max_length=50, null=True)),
                ('fotoAr', models.ImageField(upload_to='img/')),
                ('descAr', models.CharField(max_length=250)),
                ('fechaIngr', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='vistaobra',
            name='imgVista',
            field=models.ImageField(upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='vistaobra',
            name='nombreV',
            field=models.CharField(max_length=50),
        ),
    ]
