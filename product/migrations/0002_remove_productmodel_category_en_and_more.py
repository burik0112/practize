# Generated by Django 4.0.6 on 2022-08-17 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='category_en',
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='category_ru',
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='category_uz',
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='tags_en',
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='tags_ru',
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='tags_uz',
        ),
    ]