# Generated by Django 3.1.5 on 2021-02-15 18:05

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_about_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='name',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='about',
            name='role',
            field=tinymce.models.HTMLField(),
        ),
    ]
