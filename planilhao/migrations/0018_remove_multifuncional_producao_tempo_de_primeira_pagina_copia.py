# Generated by Django 3.0.8 on 2020-08-28 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planilhao', '0017_auto_20200828_1921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='multifuncional_producao',
            name='tempo_de_primeira_pagina_copia',
        ),
    ]
