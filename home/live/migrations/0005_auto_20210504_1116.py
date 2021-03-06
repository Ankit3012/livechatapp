# Generated by Django 3.0.7 on 2021-05-04 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('live', '0004_closeticket'),
    ]

    operations = [
        migrations.CreateModel(
            name='headprofile',
            fields=[
                ('hid', models.IntegerField(primary_key=True, serialize=False)),
                ('headname', models.CharField(max_length=42)),
            ],
        ),
        migrations.AlterField(
            model_name='closeticket',
            name='creceiver_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creceiver', to='live.headprofile'),
        ),
        migrations.AlterField(
            model_name='closeticket',
            name='csender_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='csender', to='live.headprofile'),
        ),
        migrations.AlterField(
            model_name='openticket',
            name='oreceiver_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oreceiver', to='live.headprofile'),
        ),
        migrations.AlterField(
            model_name='openticket',
            name='osender_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='osender', to='live.headprofile'),
        ),
    ]
