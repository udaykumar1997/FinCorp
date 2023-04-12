# Generated by Django 4.2 on 2023-04-12 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Folio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ModeOfPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(max_length=500)),
                ('transaction_class', models.CharField(choices=[('WMBU', 'White, mbu'), ('BMBU', 'Black, mbu'), ('WMMA', 'White, mma')], max_length=4)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FinCorp.currency')),
                ('folio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FinCorp.folio')),
                ('mode_of_payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FinCorp.modeofpayment')),
                ('transaction_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FinCorp.transactiongroup')),
            ],
        ),
    ]
