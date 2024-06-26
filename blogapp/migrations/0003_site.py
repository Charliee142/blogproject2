# Generated by Django 5.0.4 on 2024-04-11 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_alter_post_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='image/')),
            ],
            options={
                'verbose_name_plural': 'site',
            },
        ),
    ]
