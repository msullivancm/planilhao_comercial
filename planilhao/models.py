from django.db import models

# Create your models here.
class Dispositivo(models.Model):
    class Meta:
        abstract = True
    fabricante = models.CharField(max_length=200)#
    modelo = models.CharField(max_length=200)#
    processador = models.CharField(max_length=200)#Processador 
    memoria_minima = models.CharField(max_length=200)#Memória mínima / máxima
    disco_rigido = models.CharField(max_length=200)#Disco Rígido 
    interface_padrao = models.CharField(max_length=200)#Interface Padrão
    interface_opcional = models.CharField(max_length=200)#Interface Opcional 
    interface_wireless = models.CharField(max_length=200)#Interface Wireless 
    sistema_operacional = models.CharField(max_length=200)#Sistema Operacional 
    foto = models.ImageField(upload_to = 'imagens/', default = 'imagens/None/no-img.jpg')
    catalogo = models.FileField(upload_to='catalogos/', default = 'catalogos/None/no-img.jpg')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class ImpDisp(Dispositivo):
    class Meta:
        abstract = True
    colorida = models.BooleanField()
    a4 = models.BooleanField()
    a3 = models.BooleanField()
    tecnologia_de_impressao = models.CharField(max_length=200)#Tecnologia de Impressão 
    velocidade_de_impressao = models.CharField(max_length=200)#Velocidade de impressão 
    tempo_de_primeira_pagina = models.CharField(max_length=200)#Tempo de Primeira Página 
    resolucao_de_impressao = models.CharField(max_length=200)#Resolução de Impressão 
    ciclo_mensal = models.CharField(max_length=200)#Ciclo Mensal 
    linguagem_de_impressao = models.CharField(max_length=200)#Linguagem de Impressão 
    frente_e_verso_automatico = models.CharField(max_length=200)#Frente e Verso Automático 
    painel = models.CharField(max_length=200)#Painel 
    bandeja_de_entrada_de_papel = models.CharField(max_length=200)#Bandeja de Entrada de Papel 
    capacidade_maxima_de_bandejas = models.CharField(max_length=200)#Capacidade Máxima de Bandejas Opcional 
    bandeja_multiuso = models.CharField(max_length=200)#Bandeja Multiuso 
    bandeja_de_saida = models.CharField(max_length=200)#Bandeja de Saída 
    suporta_tamanho = models.CharField(max_length=200)#Suporta Tamanho A4, Carta e Ofício 
    gramatura_na_bandeja_principal = models.CharField(max_length=200)#Gramatura na Bandeja Principal 
    gramatura_na_bandeja_multiuso = models.CharField(max_length=200)#Gramatura na Bandeja Multiuso 
    
class Multifuncional(ImpDisp):
    id_multifuncional = models.AutoField(primary_key=True)
    velocidade_de_fax = models.CharField(max_length=200)#Velocidade de Fax 
    resolucao = models.CharField(max_length=200)#Resolução 
    memoria_de_fax = models.CharField(max_length=200)#Memória de Fax 
    capacidade_de_folhas_no_adf = models.CharField(max_length=200)
    bandeja_de_entrada_de_papel = models.CharField(max_length=200)
    capacidade_maxima_de_bandejas_opcional = models.CharField(max_length=200)
    bandeja_multiuso = models.CharField(max_length=200)
    def __str__(self):
        return self.multifuncional 

class Multifuncional_Producao(ImpDisp):
    id_multifuncional = models.AutoField(primary_key=True)
    velocidade_de_copia = models.CharField(max_length=200)#Velocidade de Cópia 
    tempo_de_primeira_pagina_copia = models.CharField(max_length=200)#Tempo de Primeira Página 
    resolucao_de_copia = models.CharField(max_length=200)#Resolução de cópia 
    ampliacao_e_reducao = models.CharField(max_length=200)#Ampliação e Redução 
    copias_multiplas = models.CharField(max_length=200)#Cópias Múltiplas 
    velocidade_de_digitacao = models.CharField(max_length=200)#Velocidade de Digitalização 
    compatibilidade = models.CharField(max_length=200)#Compatibilidade 
    resolucao = models.CharField(max_length=200)#Resolução 
    destino_de_saida = models.CharField(max_length=200)#Destino de Saída 
    formatos_de_saida = models.CharField(max_length=200)#Formatos de Saída
    tamanho_do_vidro = models.CharField(max_length=200)#Tamanho do Vidro 
    tamanho_do_adf = models.CharField(max_length=200)#Tamanho do ADF 
    tipo_da_passagem_do_adf = models.CharField(max_length=200)#Tipo de Passagem do ADF
    def __str__(self):
        return self.multifuncional 


class Impressora(ImpDisp):
    id_impressora = models.AutoField(primary_key=True)  # Field name made lowercase.
    def __str__(self):
        return self.impressora

