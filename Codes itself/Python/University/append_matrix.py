# Armazenando nomes em vetores:
# names = []
# name_quantity = 3
# for name in range(name_quantity):
#     foda = str(input('Write the name: '))
#     names.append(name)

# print(name)
    
# Matriz em python
linhas = 2
colunas = 2
matriz = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        nome = input('Escreva o nome: ')
        linha.append(nome)
    matriz.append(linha)

print('Matriz de nomes: ')
for linha in matriz:
    print(linha)
        
