# Generated by Django 4.1.7 on 2023-03-22 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_profile_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_url',
            field=models.ImageField(default='https://randomuser.me/api/portraits/women/93.jpg', null=True, upload_to=''),
        ),
    ]
