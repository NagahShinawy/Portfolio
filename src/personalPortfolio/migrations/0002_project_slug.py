# Generated by Django 3.1.4 on 2020-12-23 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalPortfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(default='', max_length=200),
        ),
    ]
