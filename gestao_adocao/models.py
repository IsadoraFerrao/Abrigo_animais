from django.db import models
from django.core.exceptions import ValidationError

class Adotante(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)  # Nome do adotante
    cpf = models.CharField(max_length=11, unique=True)  # CPF do adotante
    idade = models.IntegerField()  # Idade do adotante
    telefone = models.CharField(max_length=15)  # Telefone do adotante
    email = models.EmailField(max_length=50, unique=True)  # E-mail do adotante
    endereco = models.CharField(max_length=50)  # Endereço do adotante
    termo_responsabilidade = models.BooleanField(default=False)  # Indica se o adotante aceitou o termo de responsabilidade
    espaco = models.BooleanField(default=False)  # Indica se o adotante possui espaço adequado para o animal
    tempo = models.BooleanField(default=False)  # Indica se o adotante possui tempo disponível para cuidar do animal
    ciente_custos = models.BooleanField(default=False)  # Indica se o adotante está ciente dos custos para manter o animal
    disposicao_fisica_emocional = models.BooleanField(default=False)  # Indica se o adotante possui disposição física e emocional para cuidar do animal

    def clean(self):
        # Verifica se o adotante tem mais de 18 anos
        if self.idade < 18:
            raise ValidationError("Você deve ter pelo menos 18 anos para adotar um pet.")
        # Verifica se o adotante concorda com o termo de responsabilidade e preenche todos os requisitos
        if self.espaco and self.tempo and self.ciente_custos and self.disposicao_fisica_emocional:
            self.termo_responsabilidade = True
        else:
            self.termo_responsabilidade = False
            raise ValidationError("Infelizmente você não possui os requisitos necessários para adotar um pet.")

    def __str__(self): 
        return f'{self.nome}, {self.email}, {self.telefone}, {self.termo_responsabilidade}'
    
    class Meta: 
        verbose_name = 'Adotante'
        verbose_name_plural = 'Adotantes'
        ordering = ['nome'] 

class Adocao(models.Model):
    id = models.AutoField(primary_key=True)
    adotante = models.ForeignKey(Adotante, on_delete=models.PROTECT)  # Adotante associado à adoção
    termo_aceito = models.BooleanField(default=False)  # Indica se o termo de responsabilidade foi aceito
    data = models.DateTimeField(auto_now_add=True)  # Data da adoção
    
    def save(self, *args, **kwargs):
        # Verifica se há um adotante associado à adoção e atribui o valor do termo de responsabilidade
        if self.adotante:  
            self.termo_aceito = self.adotante.termo_responsabilidade  
        super().save(*args, **kwargs) 
    
    def __str__(self):
        return f'{self.adotante}, {self.termo_aceito}'
    
    class Meta: 
        verbose_name = 'Adocao'
        verbose_name_plural = 'Adocoes'
        ordering = ['-data']
