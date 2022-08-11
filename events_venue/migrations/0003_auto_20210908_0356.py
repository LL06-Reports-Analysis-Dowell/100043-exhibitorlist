# Generated by Django 3.1.2 on 2021-09-08 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events_venue', '0002_auto_20210907_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='BDEventID',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='city',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='country',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='logo',
            field=models.ImageField(upload_to='events'),
        ),
    ]