# Generated by Django 2.2.13 on 2020-11-17 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0061_auto_20201116_1757'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asset',
            options={'ordering': ['hostname', 'ip'], 'verbose_name': 'Asset'},
        ),
    ]