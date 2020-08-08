# Generated by Django 3.0.6 on 2020-08-07 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('songFile', models.FileField(upload_to='home/music')),
                ('songName', models.CharField(max_length=500)),
                ('image', models.ImageField(blank=True, upload_to='home/images/songimages')),
            ],
        ),
    ]
