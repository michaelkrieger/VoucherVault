# Generated by Django 4.2.13 on 2024-07-07 15:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


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
                ('name', models.CharField(max_length=255)),
                ('redeem_code', models.CharField(max_length=50)),
                ('store', models.CharField(max_length=255)),
                ('issue_date', models.DateField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateField()),
                ('description', models.TextField(blank=True, null=True)),
                ('code_type', models.CharField(choices=[('barcode', 'EAN13 Barcode'), ('qrcode', 'QR Code')], max_length=7)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GiftCard',
            fields=[
                ('voucher_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myapp.voucher')),
                ('initial_balance', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            bases=('myapp.voucher',),
        ),
        migrations.CreateModel(
            name='Expenditure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('gift_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenditures', to='myapp.giftcard')),
            ],
        ),
    ]
