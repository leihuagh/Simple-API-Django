# Generated by Django 2.1.2 on 2018-10-11 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20181011_0316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]