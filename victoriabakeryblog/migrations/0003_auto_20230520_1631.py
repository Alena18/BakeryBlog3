# Generated by Django 3.2.19 on 2023-05-20 16:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('victoriabakeryblog', '0002_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipepost',
            name='hearts',
            field=models.ManyToManyField(blank=True, related_name='blogpost_heart', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
