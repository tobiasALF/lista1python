s0 = 2  # Posição inicial em metros
v0 = 3  # Velocidade inicial em m/s
a = 10  # Aceleração em m/s²

tempo = float(input("Digite o tempo em segundos: "))

s = s0 + v0 * tempo + (0.5 * a * tempo**2)

print("O espaço percorrido é:")
print(s, "metros")