# Generated by Django 4.2.6 on 2024-01-13 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0071_alter_customer_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailchangerequest',
            name='confirmationKey',
            field=models.CharField(max_length=250),
        ),
    ]
