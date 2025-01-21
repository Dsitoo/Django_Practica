# Generated by Django 5.1.4 on 2025-01-15 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0020_alter_usuario_options_alter_usuario_managers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='rol',
        ),
        migrations.AddField(
            model_name='usuario',
            name='biografia',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
