# Generated by Django 2.2.2 on 2019-06-23 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190624_0004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='file',
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]