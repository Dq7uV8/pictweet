# Generated by Django 3.1 on 2020-09-23 11:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tweetapp', '0002_pictweetmodel_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictweetmodel',
            name='author',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
