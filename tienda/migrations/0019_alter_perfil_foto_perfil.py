# Generated by Django 5.1.4 on 2025-01-15 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0018_alter_perfil_foto_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='foto_perfil',
            field=models.ImageField(default='uploads/avatars/default.jpg', upload_to='uploads/avatars/'),
        ),
    ]
