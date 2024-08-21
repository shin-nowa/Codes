#Escrever um programa que dá o valor hora de um funcioonario a partir do salário mensal e horas trabalhadas no mês.

salario_mensal = input('Qual o salario mensal? ')
horas_no_mes = input('Quantas horas você trabalha no mês? ')

valor_hora = float(salario_mensal) / float(horas_no_mes)
print(valor_hora)