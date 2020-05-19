# Generated by Django 3.0.5 on 2020-05-08 16:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='register_details',
            fields=[
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('mailid', models.EmailField(max_length=50)),
                ('pswrd', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='invite_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_slot', models.TimeField()),
                ('meeting_length', models.PositiveIntegerField(default=0)),
                ('agenda', models.CharField(max_length=50)),
                ('invitees', models.ManyToManyField(error_messages={'required': 'No record found!'}, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]