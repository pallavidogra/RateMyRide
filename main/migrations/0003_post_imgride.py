# Generated by Django 2.2.7 on 2019-11-30 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imgRide',
            field=models.ImageField(default=0, upload_to='rate-my-ride'),
            preserve_default=False,
        ),
    ]
