# Generated by Django 4.1.7 on 2023-03-22 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_user_profile_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_url',
            field=models.ImageField(default='https://randomuser.me/api/portraits/men/62.jpg', null=True, upload_to=''),
        ),
    ]
