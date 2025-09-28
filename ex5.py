#escreva um algoritmo que recebe um número x e y e imprime x^y. lembre-se que ∗∗ representa a potência entre dois números em python.

numx = float(input("Digite um número que será a base do cálculo: ")) 
numy = float(input("Digite outro número que será o expoente do cálculo: "))

#** Calcula a potência
result = numx ** numy

print(f"O resultado de {numx}^{numy} é {result}.")