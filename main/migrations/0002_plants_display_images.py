# Generated by Django 3.2.4 on 2021-10-29 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plants',
            name='display_images',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
