from django.db import models

# Create your models here.

class Genero(models.Model):
    nome_genero = models.CharField(max_length=255)
    def __str__(self):
        return self.nome_genero

class Plataforma(models.Model):
    nome_plataforma = models.CharField(max_length=255)
    def __str__(self):
        return self.nome_plataforma

class Jogo(models.Model):
    nome_jogo = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    data_lancamento = models.DateField()
    destaque = models.BooleanField(default=False)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    plataformas = models.ManyToManyField(Plataforma, blank=True)
    def __str__(self):
        return self.nome_jogo

class Avaliacao(models.Model):
    nome_visitante = models.CharField(max_length=255)
    class Nota(models.IntegerChoices):
        UM = 1
        DOIS = 2
        TRES = 3
        QUATRO = 4
        CINCO = 5
    nota = models.IntegerField(choices=Nota)
    comentario = models.TextField(blank=True, null=True)
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE, related_name='avaliacoes')
    def __str__(self):
        return self.nome_visitante