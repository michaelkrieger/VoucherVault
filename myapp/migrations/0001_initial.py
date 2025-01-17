# Generated by Django 4.2.13 on 2024-07-14 22:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('voucher', 'Voucher'), ('giftcard', 'Gift Card'), ('coupon', 'Coupon')], max_length=50)),
                ('name', models.CharField(max_length=255)),
                ('redeem_code', models.CharField(max_length=50)),
                ('pin', models.CharField(blank=True, max_length=10, null=True)),
                ('issuer', models.CharField(max_length=50)),
                ('issue_date', models.DateField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateField()),
                ('description', models.TextField(blank=True, null=True)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_used', models.BooleanField(default=False)),
                ('qr_code_base64', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apprise_urls', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=255)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='myapp.item')),
            ],
        ),
    ]
