# Generated by Django 3.2 on 2021-04-16 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LegalService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Краткое описание')),
                ('is_published_landing', models.BooleanField(default=False, verbose_name='Услуга опубликована')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
                'ordering': ['title', '-date_created'],
            },
        ),
    ]
