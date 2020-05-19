# Generated by Django 3.0.5 on 2020-05-10 15:50

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('login_pg', '0004_auto_20200510_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invite_form',
            name='invitees',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('kesha', 'kesha'), ('sweta', 'sweta'), ('kishor', 'kishor'), ('priyav', 'priyav')], max_length=25),
        ),
    ]