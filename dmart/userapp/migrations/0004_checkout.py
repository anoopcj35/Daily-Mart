# Generated by Django 4.1.4 on 2023-03-17 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_cartdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=90)),
                ('productquantity', models.IntegerField()),
                ('purchasetotal', models.IntegerField()),
                ('cartid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.cartdb')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.register')),
            ],
        ),
    ]