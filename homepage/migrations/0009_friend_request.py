# Generated by Django 3.1.8 on 2022-01-13 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_auto_20220111_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='friend_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=99)),
                ('name', models.CharField(max_length=99)),
                ('friend_username', models.CharField(max_length=99)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
