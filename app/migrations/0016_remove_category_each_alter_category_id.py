# Generated by Django 4.0.3 on 2022-04-14 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_phone_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='each',
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
