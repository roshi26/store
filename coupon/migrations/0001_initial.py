# Generated by Django 2.2.12 on 2020-09-21 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.IntegerField()),
                ('quality', models.IntegerField()),
                ('issue_by', models.CharField(blank=True, max_length=200, null=True)),
                ('issue_to', models.CharField(blank=True, max_length=200, null=True)),
                ('last_updated', models.DateField(auto_now_add=True)),
                ('brand', models.CharField(blank=True, max_length=200, null=True)),
                ('quantity', models.IntegerField()),
                ('discount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Promotions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.IntegerField()),
                ('offer', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiry_date', models.DateField()),
                ('coupon_number', models.IntegerField()),
                ('issue_by', models.CharField(max_length=200)),
                ('issue_to', models.CharField(max_length=200)),
                ('created_by', models.CharField(max_length=200)),
                ('recieve_by', models.CharField(max_length=200)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coupon.Product')),
            ],
        ),
    ]