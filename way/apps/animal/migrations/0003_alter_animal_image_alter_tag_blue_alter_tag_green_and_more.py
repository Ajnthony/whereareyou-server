# Generated by Django 4.1.7 on 2023-04-05 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='image',
            field=models.ImageField(blank=True, default='https://source.unsplash.com/random/?animal', upload_to=''),
        ),
        migrations.AlterField(
            model_name='tag',
            name='blue',
            field=models.IntegerField(default=198),
        ),
        migrations.AlterField(
            model_name='tag',
            name='green',
            field=models.IntegerField(default=255),
        ),
        migrations.AlterField(
            model_name='tag',
            name='red',
            field=models.IntegerField(default=153),
        ),
    ]