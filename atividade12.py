carros_vendidos = int(input("Digite o número de carros vendidos: "))
valor_vendas    = int(input("Digite o valor total das vendas: "))
salario_fixo    = int(input("Digite o salário fixo: "))
valor_comissao_por_carro = int(input("Digite o valor de comissão por carro vendido: "))

valor_total_comissao = valor_comissao_por_carro * carros_vendidos
valor_total_vendas = 0.05 * valor_vendas

salario_final = salario_fixo + valor_total_comissao + valor_total_vendas

print("O salário final do vendedor é:", salario_final)