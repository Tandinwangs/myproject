# Generated by Django 3.0.3 on 2021-11-09 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_footer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footer',
            name='gym',
            field=models.CharField(max_length=200),
        ),
    ]
