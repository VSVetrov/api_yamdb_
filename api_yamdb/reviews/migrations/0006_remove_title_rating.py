# Generated by Django 2.2.16 on 2022-04-13 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_title_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='rating',
        ),
    ]