# Generated by Django 5.1.2 on 2024-10-26 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='dni',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AddField(
            model_name='producto',
            name='texes',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='producto',
            name='cantidad',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='producto',
            name='costo',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15),
        ),
    ]
