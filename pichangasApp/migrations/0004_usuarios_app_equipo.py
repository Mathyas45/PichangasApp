# Generated by Django 4.2.3 on 2023-08-01 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pichangasApp', '0003_alter_pichanga_app_equipo_local_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios_app',
            name='equipo',
            field=models.CharField(default='', max_length=128),
        ),
    ]