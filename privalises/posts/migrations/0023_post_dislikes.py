# Generated by Django 3.2.4 on 2021-07-03 00:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0022_auto_20210702_0437'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislikes',
            field=models.ManyToManyField(blank=True, default=None, related_name='dislikes', to=settings.AUTH_USER_MODEL),
        ),
    ]
