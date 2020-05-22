# Generated by Django 3.0.5 on 2020-05-13 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Nom',
        ),
        migrations.AddField(
            model_name='profile',
            name='NbPers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='codeP',
            field=models.CharField(default='', max_length=6),
        ),
        migrations.AddField(
            model_name='profile',
            name='numero',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='rue',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='telephone',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pics'),
        ),
    ]
