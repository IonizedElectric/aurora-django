# Generated by Django 3.0.3 on 2020-02-23 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_remove_account_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='poster',
            field=models.CharField(max_length=30),
        ),
    ]
