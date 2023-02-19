# Generated by Django 4.1.5 on 2023-02-18 19:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=300)),
                ('price', models.IntegerField()),
                ('pages', models.IntegerField(default=200)),
                ('year', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('sold_out', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('description', models.TextField(blank=True, default='', null=True)),
            ],
        ),
    ]
