# Generated by Django 4.2.10 on 2024-03-23 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
