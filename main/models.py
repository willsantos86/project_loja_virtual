from django.db import models
from django.urls import reverse

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    #data_criacao = models.DateTimeField(auto_now_add=True)
    #data_ultima_atualizacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('nome', )
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
    
    def __str__(self) -> str:
        return self.nome



class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='produtos', null=True, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    imagem = models.ImageField(upload_to='produtos/', blank=True)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    #estoque = models.PositiveIntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ('nome', )
        index_together = (('id', 'slug'),)
    
    def __str__(self) -> str:
        return self.nome


