
# Questão 1
'''
valor_1 = float(input('Insira o primeiro valor: '))
valor_2 = float(input('Insira o segundo valor: '))
if valor_1 > valor_2:
    print('O valor 1 (',valor_1, ') é maior que o valor 2.')
elif valor_1 == valor_2:
    print('Os dois valores são iguais.')
else:
    print('O valor 2 (',valor_2, ') é maior que o valor 1.')
'''
# Questão 2

'''
nome = str(input('Insira o nome do aluno: '))
nota = float(input('Insira a nota do aluno: '))
if nota >= 7:
    print(nome, 'Aprovado')
else:
    print(nome, 'Reprovado')
'''

# Questão 3

'''
valor_1 = float(input('Insira o primeiro número: '))
valor_2 = float(input('Insira o segundo número '))
soma = (valor_1 + valor_2)
valor_3 = float(input('Insira o terceiro número '))
if valor_3 > soma:
    print('O valor 3 é maior do que a soma (', soma,')')
elif valor_3 == soma:
    print('O valor 3 é maior do que a soma (', soma,')')
else:
    print('O valor 3 é menor do que a soma.')
'''

# Questão 4 - Dúvida: como voltar para o inicio do programa caso o input seja inválido
'''
inicial_operadora = ('c', 'v', 'o', 't')
operadora = str.lower(input('Insira a inicial da sua operadora: '))
if operadora == 'c':
    print('Sua operadora é a claro.')
elif operadora =='v':
    print('Sua operadora é a vivo.')
elif operadora == 'o':
    print('Sua operadora é a Oi')
elif operadora == 't':
    print('Sua operadora é a TIM')
else:
    print('Insira uma operadora válida: [c], [v], [o], [t]')
'''
# Questão 5 e 6

'''
nota_1 = float(input('Insira a primeira nota: '))
nota_2 = float(input('Insira a segunda nota: '))
media = ((nota_1 + nota_2)/ 2)
if media >= 7:
    print('Aprovado.')
elif media >= 4:
    print('Final.')
else:
    print('Reprovado.')
'''

# Questão 7

'''
instrumento = str.upper(input('Qual instrumento o cliente irá comprar? '))
if instrumento == 'G':
    print('A guitarra custará 1000 reais.')
elif instrumento == 'V':
    print('O violão custará 800 reais.')
elif instrumento == 'B':
    print('A bateria custará 3000 reais.')
elif instrumento == 'P':
    print('O pandeiro custará 200 reais.')
else:
    print('Insira um código de instrumento válido: [G], [V], [B], [P]')
'''