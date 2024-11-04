from django.db import models
from django.contrib.auth.models import User

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    biografia = models.TextField(blank=True)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=[('DISPONIVEL', 'Disponível'), ('EMPRESTADO', 'Emprestado')])

    def __str__(self):
        return self.titulo

class Emprestimo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.usuario} - {self.livro}"
