# Generated by Django 5.0.3 on 2024-04-02 04:36

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsfeed',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='news_image')),
                ('caption', models.CharField(max_length=300)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
