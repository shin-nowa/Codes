'''
Problema do sorvete, programei em python.
'''
chocolate_venda = float(input('Quantos litros de chocolate foram vendidos? '))
chocolate_estoque = float(input('Quantos litros de chocolate tem no estoque? '))
baunilha_venda = float(input('Quantos litros de baunilha foram vendidos? '))
baunilha_estoque = float(input('Quantos litros de baunilha tem no estoque? '))
flocos_venda = float(input('Quantos litros de flocos foram vendidos? '))
flocos_estoque = float(input('Quantos litros de flocos tem no estoque? '))
coco_venda = float(input('Quantos litros de coco foram vendidos? '))
coco_estoque = float(input('Quantos litros de coco tem no estoque? '))
tapioca_venda = float(input('Quantos litros de tapioca foram vendidos? '))
tapioca_estoque = float(input('Quantos litros de tapioca tem no estoque? '))
menta_venda = float(input('Quantos litros de menta foram vendidos? '))
menta_estoque = float(input('Quantos litros de menta tem no estoque? '))
soma_venda = (chocolate_venda + baunilha_venda + flocos_venda + coco_venda + tapioca_venda + menta_venda)
soma_estoque = (chocolate_estoque + baunilha_estoque + flocos_estoque + coco_estoque + tapioca_estoque + menta_estoque)
media_venda = soma_venda/6
media_estoque = soma_estoque/6
valor_arrecadado = soma_venda*50
valor_estoque = soma_estoque*20
# vendas = [chocolate_venda, baunilha_venda, flocos_venda, coco_venda, tapioca_venda, menta_venda]
estoque = {'chocolate': chocolate_estoque, 'baunilha': baunilha_estoque, 'flocos': flocos_estoque, 'coco':coco_estoque, 'tapioca': tapioca_estoque, 'menta': menta_estoque
}
vendas = {
    'chocolate': chocolate_venda, 'baunilha': baunilha_venda, 'flocos': flocos_venda, 'coco': coco_venda, 'tapioca': tapioca_venda, 'menta': menta_venda
}
print('A média de litros vendidos é de:',media_venda)
print('A média de litros no estoque é de: ',media_estoque)
sabor_mais_vendido = max(vendas, key=lambda x: vendas[x])
sabor_estoque = max(estoque, key=lambda x: estoque[x])
print('O sabor que mais teve vendas é:',sabor_mais_vendido)
print('O sabor que mais tem disponibilidade no estoque é:',sabor_estoque)
if soma_venda > soma_estoque:
    print('A quantidade de sorvete vendida é maior do que quantidade que há no estoque.')
elif soma_venda == soma_estoque:
    print('A quantidade de sorvete vendida é a mesma quantidade que tem no estoque.')
else:
    print('A quantidade no estoque é maior do que a quantidade de vendas.')
print('A empresa arrecadou um total de :',valor_arrecadado)
print('E no estoque a empresa tem um total de ',valor_estoque,'reais')