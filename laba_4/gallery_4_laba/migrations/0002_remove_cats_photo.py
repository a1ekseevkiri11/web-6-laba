# Generated by Django 5.0 on 2024-02-03 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_4_laba', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cats',
            name='photo',
        ),
    ]