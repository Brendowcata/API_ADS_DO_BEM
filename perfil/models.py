from tabnanny import verbose
from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.translation import gettext_lazy as _

class Perfil(TimeStampedModel):

    class UFS(models.TextChoices):
        SC = 'SC', _('Santa Catarina')
        RS = 'RS', _('Rio Grande do Sul')
        SP = 'SP', _('São Paulo')

    nome_instituicao = models.CharField(max_length=14, db_column="NOME_INSTITUIÇÂO")
    cnpj = models.CharField(max_length=14, validators=[MinLengthValidator(14), MaxLengthValidator(14)], db_column="CNPJ")
    logradouro = models.CharField(max_length=20, db_column="LOGRADOURO")
    numero = models.CharField(max_length=4, validators=[MinLengthValidator(1), MaxLengthValidator(4)], db_column="NUMERO")
    complemento = models.CharField(max_length=20, null=True, db_column="COMPLEMENTO")
    bairro = models.CharField(max_length=20, db_column="BAIRRO")
    cidade = models.CharField(max_length=20, db_column="CIDADE")
    uf = models.CharField(max_length=2, choices=UFS.choices, db_column="UF")
    cep = models.CharField(max_length=8, validators=[MinLengthValidator(8), MaxLengthValidator(8)], db_column="CEP")
    telefone = models.CharField(max_length=11, validators=[MinLengthValidator(10), MaxLengthValidator(11)], db_column="TELEFONE")
    ano_fundacao = models.CharField(max_length=4, validators=[MinLengthValidator(4), MaxLengthValidator(4)], db_column="ANO_FUNDAÇÂO")
    total_membros = models.PositiveIntegerField(db_column="TOTAL_MEMBROS")
    nome_presidente_instituicao = models.CharField(max_length=50, db_column="NOME_PRESIDENTE_INSTITUIÇÃO")

    class Meta:
        db_table = "PERFIL"
        verbose_name = "perfil"
        verbose_name_plural = "perfis"
