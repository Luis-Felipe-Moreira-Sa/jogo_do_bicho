# Generated by Django 4.1.2 on 2022-11-01 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ifpi', '0009_alter_result_last_date_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='last_date_update',
            field=models.DateField(auto_now=True, max_length=80, null=True),
        ),
    ]
