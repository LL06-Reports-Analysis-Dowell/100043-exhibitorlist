# Generated by Django 3.1.2 on 2021-11-02 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_auto_20211018_0523'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='exhibitor_link',
            field=models.URLField(default='http://asdf.com', max_length=2048),
            preserve_default=False,
        ),
    ]