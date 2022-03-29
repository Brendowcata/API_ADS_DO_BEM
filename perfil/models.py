from tabnanny import verbose
from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.translation import gettext_lazy as _

class Perfil(TimeStampedModel):

    class UFS(models.TextChoices):
        AC = 'AC', _('Acre')
        AL = 'AL', _('Alagoas')
        AP = 'AP', _('Amapa')
        AM = 'AM', _('Amazonas')
        BA = 'BA', _('Bahia')
        CE = 'CE', _('Ceara')
        ES = 'ES', _('Espirito Santo')
        GO = 'GO', _('Goias')
        MA = 'MA', _('Maranhão')
        MT = 'MT', _('Mato Grosso')
        MS = 'MS', _('Mato Grosso do Sul')
        MG = 'MG', _('Minas Gerais')
        PA = 'PA', _('Para')
        PB = 'PB', _('Paraiba')
        PR = 'PR', _('Parana')
        PE = 'PE', _('Pernambuco')
        PI = 'PI', _('Piaui')
        RJ = 'RJ', _('Rio de Janeiro')
        RN = 'RN', _('Rio Grande do Norte')
        RS = 'RS', _('Rio Grande Do Sul')
        RO = 'RO', _('Rondônia')
        RR = 'RR', _('Roraima')
        SC = 'SC', _('Santa Catarina')
        SP = 'SP', _('São Paulo')
        SE = 'SE', _('Sergipe')
        TO = 'TO', _('Tocantins')
        DF = 'DF', _('Distrito Federal')


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
