# Generated by Django 5.0 on 2024-02-03 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_4_laba', '0002_remove_cats_photo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cats',
            new_name='Cat',
        ),
    ]
