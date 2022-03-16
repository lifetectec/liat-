# Generated by Django 3.1.2 on 2021-10-25 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='broker',
            name='facebook_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='broker',
            name='instagram_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='broker',
            name='linkedin_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='broker',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='broker',
            name='pinterest_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='broker',
            name='twitter_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='broker',
            name='website_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='broker',
            name='youtube_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
