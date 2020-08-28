from django.contrib import admin
from .models import *
from .forms import *


# Register your models here.

#admin.site.register(Multifuncional)
admin.site.register(Multifuncional_Producao)
#admin.site.register(Impressora)

@admin.register(Impressora)
class ImpressoraAdmin(admin.ModelAdmin):
    list_display = ('fabricante','modelo','tecnologia_de_impressao','velocidade_de_impressao','processador','memoria_minima','disco_rigido','interface_padrao','interface_opcional','interface_wireless','tempo_de_primeira_pagina','resolucao_de_impressao','ciclo_mensal','linguagem_de_impressao','frente_e_verso_automatico','sistema_operacional','painel','bandeja_de_entrada_de_papel','capacidade_maxima_de_bandejas','bandeja_multiuso','bandeja_de_saida','suporta_tamanho','gramatura_na_bandeja_principal','gramatura_na_bandeja_multiuso','colorida','a4','a3','foto','catalogo')
    ordering = ('fabricante','modelo','tecnologia_de_impressao')
    search_fields = ('fabricante','modelo','tecnologia_de_impressao','velocidade_de_impressao','processador','memoria_minima','disco_rigido','interface_padrao','interface_opcional','interface_wireless','tempo_de_primeira_pagina','resolucao_de_impressao','ciclo_mensal','linguagem_de_impressao','frente_e_verso_automatico','sistema_operacional','painel','bandeja_de_entrada_de_papel','capacidade_maxima_de_bandejas','bandeja_multiuso','bandeja_de_saida','suporta_tamanho','gramatura_na_bandeja_principal','gramatura_na_bandeja_multiuso','colorida','a4','a3','foto','catalogo')


@admin.register(Multifuncional)
class MultifuncionalAdmin(admin.ModelAdmin):
    list_display = ('fabricante','modelo','processador','memoria_minima','disco_rigido','interface_padrao','interface_opcional','interface_wireless','sistema_operacional','foto','catalogo','uploaded_at','colorida','a4','a3','tecnologia_de_impressao','velocidade_de_impressao','tempo_de_primeira_pagina','resolucao_de_impressao','ciclo_mensal','linguagem_de_impressao','frente_e_verso_automatico','painel','bandeja_de_entrada_de_papel','capacidade_maxima_de_bandejas','bandeja_multiuso','bandeja_de_saida','suporta_tamanho','gramatura_na_bandeja_principal','gramatura_na_bandeja_multiuso','velocidade_de_fax','resolucao','memoria_de_fax','capacidade_de_folhas_no_adf','bandeja_de_entrada_de_papel','capacidade_maxima_de_bandejas_opcional','bandeja_multiuso')
    ordering = ('fabricante','modelo','tecnologia_de_impressao')
    search_fields = ('fabricante','modelo','processador','memoria_minima','disco_rigido','interface_padrao','interface_opcional','interface_wireless','sistema_operacional','foto','catalogo','uploaded_at','colorida','a4','a3','tecnologia_de_impressao','velocidade_de_impressao','tempo_de_primeira_pagina','resolucao_de_impressao','ciclo_mensal','linguagem_de_impressao','frente_e_verso_automatico','painel','bandeja_de_entrada_de_papel','capacidade_maxima_de_bandejas','bandeja_multiuso','bandeja_de_saida','suporta_tamanho','gramatura_na_bandeja_principal','gramatura_na_bandeja_multiuso','velocidade_de_fax','resolucao','memoria_de_fax','capacidade_de_folhas_no_adf','bandeja_de_entrada_de_papel','capacidade_maxima_de_bandejas_opcional','bandeja_multiuso')
    