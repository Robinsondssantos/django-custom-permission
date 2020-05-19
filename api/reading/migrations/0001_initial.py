# Generated by Django 3.0.6 on 2020-05-19 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.Device')),
            ],
        ),
    ]
