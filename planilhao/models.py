from django.db import models
from django.contrib import admin

# Create your models here.
class Dispositivo(models.Model):
    class Meta:
        abstract = True
    fabricante = models.TextField(blank=True)#
    modelo = models.TextField(blank=True)#
    processador = models.TextField(blank=True)#Processador 
    memoria_minima = models.TextField(blank=True)#Memória mínima / máxima
    disco_rigido = models.TextField(blank=True)#Disco Rígido 
    interface_padrao = models.TextField(blank=True)#Interface Padrão
    interface_opcional = models.TextField(blank=True)#Interface Opcional 
    interface_wireless = models.TextField(blank=True)#Interface Wireless 
    sistema_operacional = models.TextField(blank=True)#Sistema Operacional 
    foto = models.ImageField(upload_to = 'imagens/', default = 'imagens/None/no-img.jpg')
    catalogo = models.FileField(upload_to='catalogos/', default = 'catalogos/None/no-img.jpg')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class ImpDisp(Dispositivo):
    class Meta:
        abstract = True
    colorida = models.BooleanField()
    a4 = models.BooleanField()
    a3 = models.BooleanField()
    tecnologia_de_impressao = models.TextField(blank=True)#Tecnologia de Impressão 
    velocidade_de_impressao = models.TextField(blank=True)#Velocidade de impressão 
    tempo_de_primeira_pagina = models.TextField(blank=True)#Tempo de Primeira Página 
    resolucao_de_impressao = models.TextField(blank=True)#Resolução de Impressão 
    ciclo_mensal = models.TextField(blank=True)#Ciclo Mensal 
    linguagem_de_impressao = models.TextField(blank=True)#Linguagem de Impressão 
    frente_e_verso_automatico = models.TextField(blank=True)#Frente e Verso Automático 
    painel = models.TextField(blank=True)#Painel 
    bandeja_de_entrada_de_papel = models.TextField(blank=True)#Bandeja de Entrada de Papel 
    capacidade_maxima_de_bandejas = models.TextField(blank=True)#Capacidade Máxima de Bandejas Opcional 
    bandeja_multiuso = models.TextField(blank=True)#Bandeja Multiuso 
    bandeja_de_saida = models.TextField(blank=True)#Bandeja de Saída 
    suporta_tamanho = models.TextField(blank=True)#Suporta Tamanho A4, Carta e Ofício 
    gramatura_na_bandeja_principal = models.TextField(blank=True)#Gramatura na Bandeja Principal 
    gramatura_na_bandeja_multiuso = models.TextField(blank=True)#Gramatura na Bandeja Multiuso 
    
class Multifuncional(ImpDisp):
    id_multifuncional = models.AutoField(primary_key=True)
    velocidade_de_fax = models.TextField(blank=True)#Velocidade de Fax 
    resolucao = models.TextField(blank=True)#Resolução 
    resolucao2 = models.TextField(blank=True)#Resolução 
    memoria_de_fax = models.TextField(blank=True)#Memória de Fax 
    capacidade_de_folhas_no_adf = models.TextField(blank=True)
    bandeja_de_entrada_de_papel2 = models.TextField(blank=True)#Bandeja de Entrada de Papel 
    capacidade_maxima_de_bandejas_opcional = models.TextField(blank=True)
    bandeja_multiuso2 = models.TextField(blank=True)
    ampliacao_e_reducao = models.TextField(blank=True)#Ampliação e Redução 
    copias_multiplas = models.TextField(blank=True)#Cópias Múltiplas 
    velocidade_de_digitacao = models.TextField(blank=True)#Velocidade de Digitalização 
    compatibilidade = models.TextField(blank=True)#Compatibilidade 
    destino_de_saida = models.TextField(blank=True)#Destino de Saída 
    formatos_de_saida = models.TextField(blank=True)#Formatos de Saída
    tamanho_do_vidro = models.TextField(blank=True)#Tamanho do Vidro 
    tamanho_do_adf = models.TextField(blank=True)#Tamanho do ADF 
    tipo_da_passagem_do_adf = models.TextField(blank=True)#Tipo de Passagem do ADF
    def __str__(self):
        return self.modelo 

class Multifuncional_Producao(ImpDisp):
    id_multifuncional = models.AutoField(primary_key=True)
    velocidade_de_copia = models.TextField(blank=True)#Velocidade de Cópia 
    tempo_de_primeira_pagina_copia = models.TextField(blank=True)#Tempo de Primeira Página 
    resolucao_de_copia = models.TextField(blank=True)#Resolução de cópia 
    ampliacao_e_reducao = models.TextField(blank=True)#Ampliação e Redução 
    copias_multiplas = models.TextField(blank=True)#Cópias Múltiplas 
    velocidade_de_digitacao = models.TextField(blank=True)#Velocidade de Digitalização 
    compatibilidade = models.TextField(blank=True)#Compatibilidade 
    resolucao = models.TextField(blank=True)#Resolução 
    destino_de_saida = models.TextField(blank=True)#Destino de Saída 
    formatos_de_saida = models.TextField(blank=True)#Formatos de Saída
    tamanho_do_vidro = models.TextField(blank=True)#Tamanho do Vidro 
    tamanho_do_adf = models.TextField(blank=True)#Tamanho do ADF 
    tipo_da_passagem_do_adf = models.TextField(blank=True)#Tipo de Passagem do ADF
    def __str__(self):
        return self.modelo 


class Impressora(ImpDisp):
    id_impressora = models.AutoField(primary_key=True)  # Field name made lowercase.
    def __str__(self):
        return self.modelo

