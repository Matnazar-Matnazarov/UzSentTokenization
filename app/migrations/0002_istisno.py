# Generated by Django 5.1.6 on 2025-02-27 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Istisno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_istisno', models.CharField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Istisno',
                'verbose_name_plural': 'Istisno',
                'indexes': [models.Index(fields=['word_istisno'], name='word_istisno')],
            },
        ),
    ]
