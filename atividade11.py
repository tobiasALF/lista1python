custo_fabrica = int(input("Digite o custo de fábrica do carro: "))

percentual_distribuidor = 0.28
impostos = 0.45

custo_distribuidor = custo_fabrica * percentual_distribuidor
custo_impostos = custo_fabrica * impostos

custo_final = custo_fabrica + custo_distribuidor + custo_impostos

print("O custo final ao consumidor é:", custo_final)