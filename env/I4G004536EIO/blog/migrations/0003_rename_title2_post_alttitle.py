# Generated by Django 4.0.5 on 2022-07-04 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_title2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title2',
            new_name='alttitle',
        ),
    ]
