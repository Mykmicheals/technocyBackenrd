# Generated by Django 4.0.3 on 2022-04-14 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_alter_phone_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='media')),
            ],
            options={
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.AddField(
            model_name='laptops',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.brand'),
        ),
        migrations.AddField(
            model_name='phone',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.brand'),
        ),
        migrations.AddField(
            model_name='popularproducts',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.brand'),
        ),
        migrations.AddField(
            model_name='television',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.brand'),
        ),
    ]
