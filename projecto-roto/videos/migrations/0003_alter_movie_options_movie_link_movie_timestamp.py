# Generated by Django 4.1.3 on 2022-11-26 09:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_movie_profile_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AddField(
            model_name='movie',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Direccion del Trailer'),
        ),
        migrations.AddField(
            model_name='movie',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
