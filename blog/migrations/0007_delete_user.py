# Generated by Django 4.0.4 on 2022-05-09 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
