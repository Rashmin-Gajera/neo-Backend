# Generated by Django 3.0.4 on 2020-05-19 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0005_billingprofile_stripe_costumer_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billingprofile',
            old_name='stripe_costumer_id',
            new_name='stripe_customer_id',
        ),
    ]
