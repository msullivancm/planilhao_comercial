# Generated by Django 3.0.8 on 2020-08-28 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planilhao', '0015_multifuncional_producao_capacidade_maxima_de_bandejas_opcional'),
    ]

    operations = [
        migrations.AddField(
            model_name='multifuncional_producao',
            name='bandeja_multiuso2',
            field=models.TextField(blank=True),
        ),
    ]
