# Generated by Django 3.1.2 on 2021-10-18 05:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('exhibitors', '0004_auto_20210916_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibitor',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
