from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower


class Hospitalization(models.Model):
    IdLeito = models.CharField(primary_key=True, max_length=17, verbose_name='IdLeito')
    NomeLeito = models.CharField(max_length=10, blank=True, null=True, verbose_name='NomeLeito')
    IdQuarto = models.CharField(max_length=10, blank=True, null=True, verbose_name='IdQuarto')
    NomeQuarto = models.CharField(max_length=50, blank=True, null=True, verbose_name='NomeQuarto')
    IdSetor = models.CharField(max_length=10, blank=True, null=True, verbose_name='IdSetor')
    NomeSetor = models.CharField(max_length=50, blank=True, null=True, verbose_name='NomeSetor')
    IdPaciente = models.CharField(max_length=17, verbose_name='IdPaciente')
    NomePaciente = models.CharField(max_length=17, verbose_name='NomePaciente')
    IdInternacao = models.CharField(max_length=17, verbose_name='IdInternacao')
    DocumentoPrincipal = models.CharField(max_length=20, blank=True, null=True, verbose_name='DocumentoPrincipal')
    DocumentoSecundario = models.CharField(max_length=20, blank=True, null=True, verbose_name='DocumentoSecundario')
    DataInternacao = models.DateField(blank=True, null=True, verbose_name='DataInternacao')
    DataNascimento = models.DateField(blank=True, null=True, verbose_name='DataNascimento')
    DataAlta = models.DateField(blank=True, null=True, verbose_name='DataAlta')
    Sexo = NomeQuarto = models.CharField(max_length=10, blank=True, null=True, verbose_name='Sexo')
    Observacao = models.CharField(max_length=200, blank=True, null=True, verbose_name='Observacao')
    NomeSocial = models.CharField(max_length=17, verbose_name='NomeSocial')
    DocumentoSecundarioComplemento = models.CharField(max_length=20,blank=True,null=True, verbose_name='DocumentoSecundarioComplemento')
    NomeMae = models.CharField(max_length=50, verbose_name="NomeMae")
    IdConvenio = models.CharField(max_length=20, blank=True, null=True, verbose_name='IdConvenio')
    NomeConvenio = models.CharField(max_length=20, blank=True, null=True, verbose_name='NomeConvenio')
    IdCategoria = models.CharField(max_length=20, blank=True, null=True, verbose_name='IdCategoria')
    NomeCategoria = models.CharField(max_length=20, blank=True, null=True, verbose_name='NomeCategoria')
    NomeMedicoResponsavel = models.CharField(max_length=50, blank=True, null=True, verbose_name='NomeMedicoResponsavel')
    IdExternoMedicoResponsavel = models.CharField(max_length=50, blank=True, null=True, verbose_name='IdExternoMedicoResponsavel')

    class Meta:
        managed = False
        db_table = 'vw_sdx_internacao'

    def __str__(self):
        return str(self.IdLeito)
