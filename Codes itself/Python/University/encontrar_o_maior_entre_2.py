# Encontrar o maior entre dois números.
51
primeiro_numero = input('Insira o primeiro número: ')
segundo_numero = input('Insira o segundo número: ')

if float(primeiro_numero) > float(segundo_numero):
    print(primeiro_numero, 'é maior que ', segundo_numero) # ou print('O primeiro é maior que o segundo.')
elif float(primeiro_numero) == float(segundo_numero): 
    print('Os dois números são iguais.')
else:
    print(segundo_numero, 'é maior que',primeiro_numero) # ou print('O segundo é maior que o primeiro.')
    