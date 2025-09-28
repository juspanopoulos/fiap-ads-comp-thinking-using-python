#neste mês, João recebeu um aumento no salário, porém ele não sabe calcular o percentual de aumento. você deverá escrever um algoritmo que recebe 2 números reais representando os salários antes e depois do aumento e deverá calcular e exibir o percentual de aumento que João obteve.

sal = float(input("Digite o valor do seu antigo salário: "))
sal2 = float(input("Digite o valor do seu salário atual, após o aumento: "))

aumento = sal2 - sal

x = (aumento * 100) / sal

print(f"A porcentagem do aumento do seu salário é de {x}%.")