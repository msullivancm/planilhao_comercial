# Generated by Django 3.0.9 on 2020-08-06 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='impressora',
            fields=[
                ('colorida', models.BooleanField()),
                ('a4', models.BooleanField()),
                ('a3', models.BooleanField()),
                ('tecnologia_de_impressao', models.CharField(max_length=200)),
                ('velocidade_de_impressao', models.CharField(max_length=40)),
                ('tempo_de_primeira_pagina', models.CharField(max_length=40)),
                ('resolucao_de_impressao', models.CharField(max_length=40)),
                ('ciclo_mensal', models.CharField(max_length=40)),
                ('linguagem_de_impressao', models.CharField(max_length=40)),
                ('frente_e_verso_automatico', models.CharField(max_length=40)),
                ('painel', models.CharField(max_length=40)),
                ('bandeja_de_entrada_de_papel', models.CharField(max_length=40)),
                ('capacidade_maxima_de_bandejas', models.CharField(max_length=40)),
                ('bandeja_multiuso', models.CharField(max_length=40)),
                ('bandeja_de_saida', models.CharField(max_length=40)),
                ('suporta_tamanho', models.CharField(max_length=40)),
                ('gramatura_na_bandeja_principal', models.CharField(max_length=40)),
                ('gramatura_na_bandeja_multiuso', models.CharField(max_length=40)),
                ('id_impressora', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
