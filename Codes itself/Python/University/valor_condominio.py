agua = []
internet = []
condominio = []
gas = []
for i in range(6):
    conta_agua = float(input("Insira o valor da conta de água do apartamento: "))
    agua.append(conta_agua)
    conta_internet = float(input("Insira o valor da internet: "))
    internet.append(conta_internet)
    valor_condominio = float(input("Insira o valor do condomínio: "))
    condominio.append(valor_condominio)
    conta_gas = float(input("Insira o valor do gás :"))
    gas.append(conta_gas)
total_agua = sum(agua)
total_internet = sum(internet)
total_condominio = sum(condominio)
total_gas = sum(gas)
print("A soma dos valores de água, internet, condomínio e gás são respectivamente: ",total_agua, total_internet, total_condominio, total_gas)
media_internet = total_internet / len(internet)
media_gas = total_gas / len(gas)
print("A média de internet paga é :",media_internet)
print("A média de gás pago é :",media_gas)
    