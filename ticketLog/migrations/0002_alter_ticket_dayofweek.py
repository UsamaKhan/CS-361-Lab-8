# Generated by Django 4.0.4 on 2022-10-25 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketLog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='dayOfWeek',
            field=models.CharField(choices=[('U', 'Sunday'), ('M', 'Monday'), ('T', 'Tuesday'), ('W', 'Wednesday'), ('R', 'Thursday'), ('F', 'Friday'), ('S', 'Saturday')], max_length=1),
        ),
    ]
