# Generated by Django 4.1.4 on 2023-03-20 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0005_remove_checkout_productquantity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='productname',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='purchasetotal',
        ),
    ]