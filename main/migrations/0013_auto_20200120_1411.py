# Generated by Django 3.0 on 2020-01-20 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20200120_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='post',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='rate', to='main.Post'),
        ),
    ]