# Generated by Django 4.2.1 on 2023-05-24 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_clothes_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothes',
            name='pre_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='clothes',
            name='description',
            field=models.TextField(),
        ),
    ]