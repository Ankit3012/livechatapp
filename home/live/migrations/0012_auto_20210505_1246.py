# Generated by Django 3.0.7 on 2021-05-05 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('live', '0011_auto_20210505_1109'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='login',
            new_name='userlogin',
        ),
    ]
