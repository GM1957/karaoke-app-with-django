# Generated by Django 3.0.6 on 2020-08-08 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_song_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='tempSong',
            fields=[
                ('TSsno', models.AutoField(primary_key=True, serialize=False)),
                ('tempSongFile', models.FileField(upload_to='home/music/tempFile')),
            ],
        ),
    ]
