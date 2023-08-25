# Generated by Django 4.2.4 on 2023-08-24 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='producto',
            name='cliente',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
    ]
