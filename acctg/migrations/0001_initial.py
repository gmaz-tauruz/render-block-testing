# Generated by Django 5.0.4 on 2024-04-16 02:12

import django.core.validators
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
            name='Voucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voucher_date', models.DateField()),
                ('payee_name', models.CharField(max_length=250)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('particulars', models.CharField(max_length=250)),
                ('bank_account', models.CharField(blank=True, max_length=50, null=True)),
                ('cheque_num', models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('cheque_date', models.DateField(blank=True, null=True)),
                ('approved_date', models.DateField(blank=True, null=True)),
                ('date_forwarded', models.DateField(blank=True, null=True)),
                ('voucher_series', models.IntegerField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('locked', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('approved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='approved_vouchers', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('voucher_date', 'payee_name'),
            },
        ),
    ]
