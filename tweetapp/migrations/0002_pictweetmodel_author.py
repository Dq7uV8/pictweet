# Generated by Django 3.1 on 2020-09-23 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweetapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pictweetmodel',
            name='author',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
