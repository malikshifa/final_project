# Generated by Django 3.1.1 on 2021-04-28 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_shape'),
    ]

    operations = [
        migrations.CreateModel(
            name='coord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('point', models.JSONField()),
            ],
        ),
    ]
