#escreva um algoritmo em python que recebe dois números inteiros e exibe: a soma desses dois números, a multiplicação, a divisão inteira e o resto da divisão inteira.

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

soma = num1 + num2
mult = num1 * num2
div = num1 / num2
resto = num1 % num2

print(f"A soma dos números digitados é {soma}, a multiplicação é {mult}, a divisão é {div} e o resto da divisão é {resto}.")