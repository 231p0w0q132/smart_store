# Generated by Django 3.2.22 on 2023-11-28 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20231127_1033'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=20)),
                ('weapone_name', models.CharField(max_length=50)),
                ('money', models.CharField(max_length=30)),
            ],
        ),
    ]