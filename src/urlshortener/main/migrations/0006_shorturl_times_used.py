# Generated by Django 3.2.8 on 2022-09-05 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_shorturl_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorturl',
            name='times_used',
            field=models.IntegerField(default=0),
        ),
    ]
