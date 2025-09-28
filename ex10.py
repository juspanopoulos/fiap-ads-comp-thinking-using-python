#Usain Bolt é o recordista mundial dos 100 metros rasos com o tempo de 9,58 segundos. Escreva um algoritmo que calcula a velocidade média em m/s e em km/h de um corredor, seu algoritmo recebe como dados de entrada a distância em metros e o tempo em segundos.

aux = input("Distancia (m): ")
distancia = float(aux)

#O comando abaixo, em essência, é o mesmo que o de cima, mas combinado/resumido.

tempo = float(input("Tempo (s): "))

velocidade_ms = distancia / tempo

distancia_km = distancia / 1000
tempo_h = tempo / 3600

velocidade_kmh = distancia_km / tempo_h

print(f"Velocidade em m/s: {velocidade_ms}")
print(f"Velocidade em km/h: {velocidade_kmh}")

