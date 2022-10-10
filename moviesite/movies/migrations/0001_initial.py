# Generated by Django 4.1.2 on 2022-10-10 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('duration', models.IntegerField()),
                ('grade', models.CharField(max_length=255)),
                ('image_url', models.CharField(max_length=2083)),
            ],
        ),
    ]
