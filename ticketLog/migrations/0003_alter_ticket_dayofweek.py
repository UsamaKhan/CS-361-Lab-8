# Generated by Django 4.0.4 on 2022-10-25 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketLog', '0002_alter_ticket_dayofweek'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='dayOfWeek',
            field=models.CharField(max_length=50),
        ),
    ]
