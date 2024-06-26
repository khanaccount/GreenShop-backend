# Generated by Django 4.2.6 on 2023-11-20 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_remove_order_firstname_remove_order_secondname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='shippingAddress',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.shippingaddress'),
        ),
    ]
