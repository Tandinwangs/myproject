# Generated by Django 3.0.3 on 2021-11-09 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20211109_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='background',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
