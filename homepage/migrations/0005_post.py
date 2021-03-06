# Generated by Django 3.1.8 on 2022-01-09 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_auto_20220109_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=99)),
                ('name', models.CharField(max_length=99)),
                ('status', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photo/')),
            ],
        ),
    ]
