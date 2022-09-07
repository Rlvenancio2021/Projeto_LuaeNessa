from django.contrib import admin
from produtos.models import Produto

# Register your models here.
class Produtos(admin.ModelAdmin):
    list_display = ('id', 'nome_produto', 'descricao', 'sku', 'gtin', 'mpn', 'ncm', 'preco_custo', 'preco_venda', 'peso', 'altura', 'largura', 'profundidade', 'disponibilidade', 'estoque_quantidade', 'categoria', 'tag_title', 'meta_tag_descricao', 'url', 'foto')
    list_display_links = ('id', 'nome_produto', 'categoria')
    search_fields = ('nome_produto', 'categoria', 'ncm',)
    list_filter = ('categoria',)
    list_per_page = 15
    
admin.site.register(Produto, Produtos)