# Generated by Django 4.0.1 on 2022-05-12 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='Address',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]