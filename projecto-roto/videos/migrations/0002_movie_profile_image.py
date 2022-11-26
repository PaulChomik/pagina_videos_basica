# Generated by Django 4.1.3 on 2022-11-21 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('sinopsis', models.TextField()),
                ('image', models.ImageField(default='img_avatar1.png', upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='img_avatar1.png', upload_to=''),
        ),
    ]
