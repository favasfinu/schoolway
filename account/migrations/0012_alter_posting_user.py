# Generated by Django 5.0.3 on 2024-03-23 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_posting_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
