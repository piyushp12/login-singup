# Generated by Django 4.0.1 on 2022-05-12 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('last', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('user', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('confirm', models.CharField(max_length=50)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
            ],
        ),
    ]