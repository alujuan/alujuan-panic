from django.db import models

class Animal (models.Model):
    nome = models.CharField(max_length=100)
    nome_dono = models.CharField(max_length=100)
    especies = models.CharField(max_length=100)
    raca = models.CharField( max_length=100)
    sexo = models.CharField(max_length=100)
    idade = models.DecimalField(max_digits=100, decimal_places=3)
    tipo_sanguineo = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animais"