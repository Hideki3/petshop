from django.db import models


class Estado(models.Model):
    nome = models.CharField(max_length=20, blank=False, null=False)
    uf = models.CharField(max_length=2, blank=False, null=False)

    def __str__(self):
        return self.uf


class Cidade(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome + ' - ' + self.estado.uf


class Pessoa(models.Model):
    class Meta:
        abstract = True

    nome = models.CharField(max_length=255, blank=False, null=False)
    contato = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.nome



class Cliente(Pessoa):
    renda = models.DecimalField(max_digits=5, decimal_places=2)
    credito = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.BooleanField()


class Fornecedor(Pessoa):
    nome_fantasia = models.CharField(max_length=255, blank=False, null=False)
    cnpj = models.CharField(max_length=14, blank=False, null=False)

class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    cep = models.CharField(max_length=8, blank=True, null=True)
    numero = models.IntegerField(blank=False, null=False)
    complemetno = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

    def __str__(self):
        return '{0} {1} {2}, {3}'.format(self.rua, self.numero, self.complemetno, self.cidade)


class Telefone(models.Model):
    numero = models.CharField(max_length=20)
    descricao = models.CharField(
        max_length=80,
        choices=[('Fixo', 'Fixo'), ('Celular', 'Celular')],
        default='Celular')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.numero



class ProdutoAbstrato(models.Model):
    class Meta:
        abstract = True

    descricao = models.CharField(max_length=255, blank=False, null=False)
    status = models.BooleanField()
    valor_venda = models.DecimalField(max_digits=5, decimal_places=2)


class Produto(ProdutoAbstrato):
    valor_compra = models.DecimalField(max_digits=5, decimal_places=2)
    codigo_barras = models.CharField(max_length=255, blank=False, null=False)
    quantidade_estoque = models.IntegerField()
    unidade_medida = models.CharField(max_length=5,
                                      choices=[('kg', 'Kg'), ('un', 'Un')],
                                      default='Un')


class Servico(ProdutoAbstrato):
    pass
