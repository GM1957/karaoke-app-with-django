# Generated by Django 3.0.6 on 2020-08-07 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200807_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='slug',
            field=models.CharField(default='', max_length=500),
        ),
    ]