# Generated by Django 2.2.6 on 2019-11-26 01:05

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('Online_Content', '0007_auto_20191125_1454'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='article_content',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
