# Generated by Django 5.1.4 on 2025-01-15 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0008_rename_especificaciones_producto_especificaciones_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen1',
            field=models.ImageField(blank=True, default='media/uploads/default_P.png', null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen2',
            field=models.ImageField(default='media/uploads/default_P.png', upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen3',
            field=models.ImageField(default='media/uploads/default_P.png', upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen4',
            field=models.ImageField(default='media/uploads/default_P.png', upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen5',
            field=models.ImageField(default='media/uploads/default_P.png', upload_to='uploads/'),
        ),
    ]
