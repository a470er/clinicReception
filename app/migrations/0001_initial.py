# Generated by Django 5.1.7 on 2025-03-23 04:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200, verbose_name='ステータスメッセージ')),
                ('processedReceptionTime', models.CharField(max_length=200, verbose_name='ステータスメッセージ')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新日')),
            ],
        ),
    ]
