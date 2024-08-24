# Generated by Django 5.1 on 2024-08-20 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentmodel',
            name='payment_method',
        ),
        migrations.AddField(
            model_name='paymentmodel',
            name='payment_menthod',
            field=models.CharField(choices=[('CASH', 'Efectivo'), ('CARD', 'Tarjeta')], default='2024-08-19 19:45:00'),
            preserve_default=False,
        ),
    ]
