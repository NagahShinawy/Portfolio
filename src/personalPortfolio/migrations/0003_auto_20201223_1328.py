# Generated by Django 3.1.4 on 2020-12-23 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalPortfolio', '0002_project_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(default='', editable=False, max_length=200, unique=True),
        ),
    ]