# Generated by Django 2.2.5 on 2019-10-04 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_fornecedor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
                ('status', models.BooleanField()),
                ('valor_venda', models.DecimalField(decimal_places=2, max_digits=5)),
                ('valor_compra', models.DecimalField(decimal_places=2, max_digits=5)),
                ('codigo_barras', models.CharField(max_length=255)),
                ('quantidade_estoque', models.IntegerField()),
                ('unidade_medida', models.CharField(choices=[('Kg', 'Kg'), ('Un', 'Un')], default='Un', max_length=5)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
