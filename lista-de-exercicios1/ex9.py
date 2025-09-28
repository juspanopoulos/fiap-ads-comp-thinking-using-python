#Dados o preço de um produto e um percentual de desconto, escreva um algoritmo que calcula e mostra o valor do desconto e o novo preço do produto dado o percentual.

preco = float(input("Preço: "))
desconto = int(input("Percentual de desconto: "))

valor_desconto = preco * (desconto / 100)

precodesc = preco - valor_desconto

print(f"Valor do desconto: {valor_desconto}")
print(f"Preço com desconto: {precodesc}")

#E se, ao invés de um desconto, fosse um aumento. O que muda no seu algoritmo?
#precodesc = preco + valor_desconto

