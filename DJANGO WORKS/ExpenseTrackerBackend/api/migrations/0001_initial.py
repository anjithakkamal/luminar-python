# Generated by Django 5.0.3 on 2024-07-25 05:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('amount', models.PositiveIntegerField()),
                ('category', models.CharField(choices=[('Housing', 'Housing'), ('Transportation', 'Transportation'), ('Food', 'Food'), ('Health', 'Health'), ('Entertainment', 'Entertainment'), ('DebtPayments', 'Debt Payments'), ('PersonalCare', 'Personal Care'), ('Education', 'Education'), ('Savings', 'Savings'), ('Miscellaneous', 'Miscellaneous')], default='Miscellaneous', max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('priority', models.CharField(choices=[('need', 'need'), ('want', 'want')], default='need', max_length=200)),
                ('user_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
