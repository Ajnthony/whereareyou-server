# Generated by Django 4.1.7 on 2023-04-05 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address_line_2',
            field=models.TextField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_url',
            field=models.ImageField(default='https://randomuser.me/api/portraits/women/78.jpg', null=True, upload_to=''),
        ),
    ]
