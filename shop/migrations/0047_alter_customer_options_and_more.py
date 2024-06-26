# Generated by Django 4.2.6 on 2023-12-27 18:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0046_rename_is_staff_customer_isstaff_customer_isactive'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='isActive',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='isStaff',
            new_name='is_staff',
        ),
        migrations.AddField(
            model_name='customer',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AddField(
            model_name='customer',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
