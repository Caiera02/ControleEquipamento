# Generated by Django 5.0 on 2024-12-19 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_ticket_finish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='finish',
        ),
    ]
