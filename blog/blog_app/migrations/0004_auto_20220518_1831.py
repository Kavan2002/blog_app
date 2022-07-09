# Generated by Django 3.1.4 on 2022-05-18 13:01

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog_app', '0003_transancation'),
    ]

    operations = [
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('transaction_status', models.BooleanField(default=False)),
                ('transaction_description', models.TextField(default=' ')),
                ('transaction_model_name', models.CharField(max_length=20)),
                ('transaction_timstamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('transaction_user_id', models.CharField(default='admin', max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='transancation',
        ),
    ]
