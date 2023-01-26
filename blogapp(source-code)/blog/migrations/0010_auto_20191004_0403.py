# Generated by Django 2.2.5 on 2019-10-03 22:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0009_auto_20191004_0232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog_reviews',
            name='author_name',
        ),
        migrations.AddField(
            model_name='blog_reviews',
            name='author',
            field=models.ForeignKey(default=None, on_delete='cascade', to=settings.AUTH_USER_MODEL),
        ),
    ]