#escreva um algoritmo que calcula a área e o perímetro do círculo, use 3.141592 como valor de π.

raio = float(input("Digite o valor do raio do círculo: "))

pi = 3.141592

area = pi * (raio ** 2)
perimetro = 2 * pi * raio

print(f"Dado o raio de {raio}, a área do círculo é {area} e o perímetro é {perimetro}.")