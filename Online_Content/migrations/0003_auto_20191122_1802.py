# Generated by Django 2.2.6 on 2019-11-23 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Online_Content', '0002_auto_20191122_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(default='Content not available'),
        ),
    ]