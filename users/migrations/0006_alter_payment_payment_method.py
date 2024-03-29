# Generated by Django 4.2 on 2024-02-24 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_payment_stripe_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(choices=[('cash', 'Наличные'), ('card', 'Картой')], default='card', max_length=30, verbose_name='Способ оплаты'),
        ),
    ]
