# Generated by Django 4.2.10 on 2024-03-23 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_remove_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
