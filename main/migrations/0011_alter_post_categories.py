# Generated by Django 4.1.1 on 2022-11-29 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_post_categories_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.CharField(default='My Tech Journey', max_length=280),
        ),
    ]