# Generated by Django 3.1.4 on 2022-04-04 14:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
