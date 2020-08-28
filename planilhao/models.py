from django.db import models
from django.contrib import admin

# Create your models here.
class Dispositivo(models.Model):
    class Meta:
        abstract = True
    fabricante = models.CharField(max_length=200, blank=True)#
    modelo = models.CharField(max_length=200, blank=True)#
    processador = models.CharField(max_length=200, blank=True)#Processador 
    memoria_minima = models.CharField(max_length=200, blank=True)#Memória mínima / máxima
    disco_rigido = models.CharField(max_length=200, blank=True)#Disco Rígido 
    interface_padrao = models.CharField(max_length=200, blank=True)#Interface Padrão
    interface_opcional = models.CharField(max_length=200, blank=True)#Interface Opcional 
    interface_wireless = models.CharField(max_length=200, blank=True)#Interface Wireless 
    sistema_operacional = models.CharField(max_length=200, blank=True)#Sistema Operacional 
    foto = models.ImageField(upload_to = 'imagens/', default = 'imagens/None/no-img.jpg')
    catalogo = models.FileField(upload_to='catalogos/', default = 'catalogos/None/no-img.jpg')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class ImpDisp(Dispositivo):
    class Meta:
        abstract = True
    colorida = models.BooleanField()
    a4 = models.BooleanField()
    a3 = models.BooleanField()
    tecnologia_de_impressao = models.CharField(max_length=200, blank=True)#Tecnologia de Impressão 
    velocidade_de_impressao = models.CharField(max_length=200, blank=True)#Velocidade de impressão 
    tempo_de_primeira_pagina = models.CharField(max_length=200, blank=True)#Tempo de Primeira Página 
    resolucao_de_impressao = models.CharField(max_length=200, blank=True)#Resolução de Impressão 
    ciclo_mensal = models.CharField(max_length=200, blank=True)#Ciclo Mensal 
    linguagem_de_impressao = models.CharField(max_length=200, blank=True)#Linguagem de Impressão 
    frente_e_verso_automatico = models.CharField(max_length=200, blank=True)#Frente e Verso Automático 
    painel = models.CharField(max_length=200, blank=True)#Painel 
    bandeja_de_entrada_de_papel = models.CharField(max_length=200, blank=True)#Bandeja de Entrada de Papel 
    capacidade_maxima_de_bandejas = models.CharField(max_length=200, blank=True)#Capacidade Máxima de Bandejas Opcional 
    bandeja_multiuso = models.CharField(max_length=200, blank=True)#Bandeja Multiuso 
    bandeja_de_saida = models.CharField(max_length=200, blank=True)#Bandeja de Saída 
    suporta_tamanho = models.CharField(max_length=200, blank=True)#Suporta Tamanho A4, Carta e Ofício 
    gramatura_na_bandeja_principal = models.CharField(max_length=200, blank=True)#Gramatura na Bandeja Principal 
    gramatura_na_bandeja_multiuso = models.CharField(max_length=200, blank=True)#Gramatura na Bandeja Multiuso 
    
class Multifuncional(ImpDisp):
    id_multifuncional = models.AutoField(primary_key=True)
    velocidade_de_fax = models.CharField(max_length=200, blank=True)#Velocidade de Fax 
    resolucao = models.CharField(max_length=200, blank=True)#Resolução 
    memoria_de_fax = models.CharField(max_length=200, blank=True)#Memória de Fax 
    capacidade_de_folhas_no_adf = models.CharField(max_length=200, blank=True)
    bandeja_de_entrada_de_papel = models.CharField(max_length=200, blank=True)
    capacidade_maxima_de_bandejas_opcional = models.CharField(max_length=200, blank=True)
    bandeja_multiuso = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.modelo 

class Multifuncional_Producao(ImpDisp):
    id_multifuncional = models.AutoField(primary_key=True)
    velocidade_de_copia = models.CharField(max_length=200, blank=True)#Velocidade de Cópia 
    tempo_de_primeira_pagina_copia = models.CharField(max_length=200, blank=True)#Tempo de Primeira Página 
    resolucao_de_copia = models.CharField(max_length=200, blank=True)#Resolução de cópia 
    ampliacao_e_reducao = models.CharField(max_length=200, blank=True)#Ampliação e Redução 
    copias_multiplas = models.CharField(max_length=200, blank=True)#Cópias Múltiplas 
    velocidade_de_digitacao = models.CharField(max_length=200, blank=True)#Velocidade de Digitalização 
    compatibilidade = models.CharField(max_length=200, blank=True)#Compatibilidade 
    resolucao = models.CharField(max_length=200, blank=True)#Resolução 
    destino_de_saida = models.CharField(max_length=200, blank=True)#Destino de Saída 
    formatos_de_saida = models.CharField(max_length=200, blank=True)#Formatos de Saída
    tamanho_do_vidro = models.CharField(max_length=200, blank=True)#Tamanho do Vidro 
    tamanho_do_adf = models.CharField(max_length=200, blank=True)#Tamanho do ADF 
    tipo_da_passagem_do_adf = models.CharField(max_length=200, blank=True)#Tipo de Passagem do ADF
    def __str__(self):
        return self.modelo 


class Impressora(ImpDisp):
    id_impressora = models.AutoField(primary_key=True)  # Field name made lowercase.
    def __str__(self):
        return self.modelo

