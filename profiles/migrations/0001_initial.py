# Generated by Django 2.1.2 on 2018-10-12 14:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('bio', models.CharField(max_length=128, null=True)),
                ('gender', models.CharField(max_length=128, null=True)),
                ('image', models.TextField(max_length=128, null=True)),
            ],
        ),
    ]
