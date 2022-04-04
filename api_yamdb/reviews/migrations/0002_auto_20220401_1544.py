# Generated by Django 2.2.16 on 2022-04-01 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titlesgenres',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='genre', to='reviews.Genre'),
        ),
        migrations.AlterField(
            model_name='titlesgenres',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='title', to='reviews.Title'),
        ),
    ]
