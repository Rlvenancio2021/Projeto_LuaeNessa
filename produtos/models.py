from django.db import models

# Create your models here.
class Produto(models.Model):
    nome_produto = models.CharField(max_length=100)
    descricao = models.TextField()
    sku = models.CharField(max_length=50)
    gtin = models.CharField(max_length=20)
    mpn = models.CharField(max_length=20)
    ncm = models.IntegerField
    preco_custo = models.FloatField()
    preco_venda = models.FloatField()
    peso = models.FloatField()
    altura = models.FloatField()
    largura = models.FloatField()
    profundidade = models.FloatField()
    OPCOES = (
        (1, '1 dia útil'),
        (2, '2 dias úteis'),
        (3, '3 dias úteis'),
        (4, '4 dias úteis'),
        (5, '5 dias úteis'),
        (6, '6 dias úteis'),
        (7, '7 dias úteis'),
        (8, '8 dias úteis'),
        (9, '9 dias úteis'),
        (10, '10 dias úteis'),
        (15, '15 dias úteis'),
        (20, '20 dias úteis'),
        (25, '25 dias úteis'),
        (30, '30 dias úteis'),
        (45, '45 dias úteis'),
        (60, '60 dias úteis'),
        (90, '90 dias úteis'),
        (2, '2 dias úteis')
    )
    disponibilidade = models.CharField(max_length=2, choices=OPCOES, blank=False, null=False, default=4)
    estoque_quantidade = models.FloatField()
    categoria = models.CharField(max_length=20)
    tag_title = models.CharField(max_length=20)
    meta_tag_descricao = models.CharField(max_length=20)
    url = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='fotos/%d/%m/%Y', blank=True)
