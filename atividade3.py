AP = int(input("Digite a altura da parede em metros: "))
LP = int(input("Digite a largura da parede em metros: "))
A  = int(input("Digite a altura do azulejo em metros: "))
LA = int(input("Digite a largura do azulejo em metros: "))

area_parede = AP * LP
area_azulejo = A * LA 

quantidade_azulejos = area_parede / area_azulejo

print("Quantidade de azulejos necessários:", int(quantidade_azulejos))
