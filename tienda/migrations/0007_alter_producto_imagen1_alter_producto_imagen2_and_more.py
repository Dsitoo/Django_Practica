# Generated by Django 5.1.4 on 2025-01-13 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0006_alter_producto_imagen1_alter_producto_imagen2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen1',
            field=models.ImageField(blank=True, default='img/img_p/default_P.png', null=True, upload_to='../static/img/img_p/'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen2',
            field=models.ImageField(default='img/img_p/default_P.png', upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen3',
            field=models.ImageField(default='img/img_p/default_P.png', upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen4',
            field=models.ImageField(default='img/img_p/default_P.png', upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen5',
            field=models.ImageField(default='img/img_p/default_P.png', upload_to='uploads/'),
        ),
    ]
