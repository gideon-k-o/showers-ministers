# Generated by Django 4.0.1 on 2022-02-16 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='help',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tille', models.CharField(max_length=200)),
                ('body', models.TextField()),
            ],
        ),
    ]
