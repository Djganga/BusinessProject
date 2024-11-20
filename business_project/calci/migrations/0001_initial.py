# Generated by Django 5.1.3 on 2024-11-20 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_name', models.CharField(max_length=100)),
                ('customer_name', models.CharField(max_length=100)),
                ('items', models.CharField(max_length=100)),
                ('bill_amount', models.DecimalField(decimal_places=2, max_digits=100)),
                ('received_amount', models.DecimalField(decimal_places=2, max_digits=100)),
                ('balance_amount', models.DecimalField(decimal_places=2, max_digits=100)),
                ('profit', models.DecimalField(decimal_places=2, max_digits=100)),
                ('created_date_time', models.DateTimeField(auto_now_add=True)),
                ('updated_date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]