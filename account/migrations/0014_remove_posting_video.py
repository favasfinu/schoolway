# Generated by Django 5.0.3 on 2024-03-26 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_posting_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posting',
            name='video',
        ),
    ]