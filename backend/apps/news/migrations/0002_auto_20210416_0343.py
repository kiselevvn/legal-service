# Generated by Django 3.2 on 2021-04-16 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Новость опубликована'),
        ),
        migrations.AlterField(
            model_name='news',
            name='is_published_landing',
            field=models.BooleanField(default=False, verbose_name='Новость опубликована на главной странице'),
        ),
    ]