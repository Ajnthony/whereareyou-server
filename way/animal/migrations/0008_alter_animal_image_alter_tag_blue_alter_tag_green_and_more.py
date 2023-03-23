# Generated by Django 4.1.7 on 2023-03-22 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0007_alter_animal_image_alter_tag_blue_alter_tag_green_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='image',
            field=models.ImageField(blank=True, default='https://source.unsplash.com/random/?cat', upload_to=''),
        ),
        migrations.AlterField(
            model_name='tag',
            name='blue',
            field=models.IntegerField(default=98),
        ),
        migrations.AlterField(
            model_name='tag',
            name='green',
            field=models.IntegerField(default=182),
        ),
        migrations.AlterField(
            model_name='tag',
            name='red',
            field=models.IntegerField(default=197),
        ),
    ]
