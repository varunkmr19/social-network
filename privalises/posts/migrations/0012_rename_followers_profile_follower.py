# Generated by Django 3.2.4 on 2021-06-19 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20210619_1728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='followers',
            new_name='follower',
        ),
    ]
