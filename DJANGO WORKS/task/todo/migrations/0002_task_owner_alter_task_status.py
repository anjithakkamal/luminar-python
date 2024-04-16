# Generated by Django 5.0.3 on 2024-04-11 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='owner',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
