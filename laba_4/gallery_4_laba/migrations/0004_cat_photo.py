# Generated by Django 5.0 on 2024-02-03 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_4_laba', '0003_rename_cats_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]
