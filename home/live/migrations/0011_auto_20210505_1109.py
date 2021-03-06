# Generated by Django 3.0.7 on 2021-05-05 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live', '0010_auto_20210505_1103'),
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('lid', models.IntegerField(primary_key=True, serialize=False)),
                ('lname', models.CharField(max_length=42)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=250)),
            ],
        ),
        migrations.RemoveField(
            model_name='ticketprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='ticketprofile',
            name='password',
        ),
    ]
