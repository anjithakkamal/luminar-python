# Generated by Django 5.0.3 on 2024-05-27 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_movie_producer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.PositiveIntegerField()),
                ('picture', models.ImageField(null=True, upload_to='image')),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=200)),
            ],
        ),
    ]
