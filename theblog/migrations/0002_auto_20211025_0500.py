# Generated by Django 3.1.2 on 2021-10-25 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='google_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='zoom_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
