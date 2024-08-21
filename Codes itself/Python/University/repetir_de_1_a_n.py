#Criar um programa que imprima os valores de 1 a N (dado pelo usuario)

valor_max = int(input('Digite até que número você quer que seja mostrado: ')) #por algum motivo o float não pega no for ali.
valor_min = 1
for n in range(valor_min, valor_max + 1):
    print(n)