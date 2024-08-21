# Questão 12.
# numero = []
# for cont in range(1,11):
#     numero.append(cont * 2)
# for num in numero:
#     print(num)

#Questao 13
# nomes_seriados = []
# quantidade_episodios = []
# eps = 0
# for ep in range(3):
#     serie1 = input("Digite o nome da série: ")
#     nomes_seriados.append(serie1)
#     episodios1 = float(input("Digite o número de episódios: "))
#     quantidade_episodios.append(episodios1)
#     eps = eps + episodios1
# media_episodios = eps / len(nomes_seriados)
# print("A média de episódios por série é: ",media_episodios)
# print("A quantidade de episódios total é de :",eps)
# maior_ep = max(quantidade_episodios)
# indice_maior_ep = quantidade_episodios.index(maior_ep)
# seriado_maior = nomes_seriados[indice_maior_ep]
# print("Seriado com mais episódios :",seriado_maior)
# nomes_seriados_r = list(reversed(nomes_seriados))
# quantidade_episodios_r = list(reversed(quantidade_episodios))
# for serie1, episodios1 in zip(quantidade_episodios_r, nomes_seriados_r):
#     print(f"Seriados: {serie1}, Episodios: {episodios1}")
#Questao 15
for i in range(0,501, 2):
    print (i)