# Generated by Django 4.1.1 on 2022-12-01 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
