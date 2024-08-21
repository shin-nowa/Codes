'''
chutar um número e ver se foi maior ou menor, e se bate com o número que foi gerado
1- valor aleátorio de 1 a 10
2- chute do usuário
3- verificar se o número chutado é maior, menor, ou igual ao número aleátorio
4- restringir se for maior do que 10, ou menor que 1
5- informar se o valor foi maior, menor ou igual.
6- gerar o número aleátorio, inputar o número do usuário, colocar as condicionais, verificar se está acima, abaixo ou igual, 

'''
import math 
import random

print('Chute um número de 1 a 100 até chegar no número que será gerado aleatoriamente.')
valor_aleatorio = random.randint(1,100)
acertou = False
while acertou == False:
    chute = int(input('Qual o seu chute? ')) #colocar o int antes caso não dê certo com a lib
    if chute > valor_aleatorio:
        print('O número que chutou é maior do que o gerado aleatoriamente.')
    elif chute == valor_aleatorio:
        print('O número que chutou é igual o gerado aleatoriamente, parabéns.')
        acertou = True
    else:
        print('O número que chutou é menor do que o gerado aleatoriamente')