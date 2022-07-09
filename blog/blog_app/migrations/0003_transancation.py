# Generated by Django 3.1.4 on 2022-05-17 13:32

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog_app', '0002_auto_20220404_1930'),
    ]

    operations = [
        migrations.CreateModel(
            name='transancation',
            fields=[
                ('transancation_id', models.AutoField(primary_key=True, serialize=False)),
                ('transancation_status', models.BooleanField(default=False)),
                ('transancation_description', models.TextField(default=' ')),
                ('transaction_model_name', models.CharField(max_length=20)),
                ('transancation_timstamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]