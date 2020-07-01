# Generated by Django 3.0 on 2020-07-01 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crawler', '0004_auto_20200701_1136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='config',
            name='channel',
        ),
        migrations.AddField(
            model_name='config',
            name='resource',
            field=models.ManyToManyField(to='Crawler.Platform', verbose_name='Resource'),
        ),
    ]