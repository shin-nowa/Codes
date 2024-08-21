'''
Fatorial de um número, imprimir um programa que recebe um número e imprime o fatorial dele.
Precisa de um número, deve ser positivo, e um valor inteiro, exibir o fatorial do número na tela. inputar, colocar as condições, fatorial = 1, loop de 1 a n
'''
numero = int(input('Número que deseja o fatorial: '))
if numero > 0:
    fatorial = 1
    for n in range(1,numero+1):
        fatorial = fatorial * n
    print("o resultado é:",fatorial)