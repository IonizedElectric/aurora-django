# Generated by Django 3.0.3 on 2020-02-21 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_post_poster'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('pword', models.CharField(max_length=64)),
                ('signup_date', models.DateTimeField(verbose_name='Date signed up')),
            ],
        ),
    ]
