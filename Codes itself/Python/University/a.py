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