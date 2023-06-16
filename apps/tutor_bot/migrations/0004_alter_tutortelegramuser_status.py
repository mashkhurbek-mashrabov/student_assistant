# Generated by Django 4.2.2 on 2023-06-15 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_bot', '0003_studentgroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutortelegramuser',
            name='status',
            field=models.IntegerField(choices=[(1, 'NEW'), (2, 'Pending'), (3, 'Approved'), (4, 'Rejected')], default=1),
        ),
    ]