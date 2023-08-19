macas      = int(input("Digite o número de maçãs compradas: "))
bananas_kg = int(input("Digite a quantidade de kg de bananas: "))

custo_macas = macas * 1.30
custo_bananas = bananas_kg * 5.00

custo_total = custo_macas + custo_bananas

print("O custo total da compra é:")
print(custo_total, "R$")