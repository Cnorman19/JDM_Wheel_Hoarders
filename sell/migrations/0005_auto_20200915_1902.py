# Generated by Django 2.2.15 on 2020-09-15 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0004_sell_offset_choices'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sell',
            old_name='offset_choices',
            new_name='offset',
        ),
    ]