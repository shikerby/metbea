# Generated by Django 2.1.5 on 2019-03-28 14:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_auto_20190306_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='users_like',
            field=models.ManyToManyField(blank=True, related_name='posts_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
