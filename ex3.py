#escreva um algoritmo que recebe o nome de uma pessoa e seu ano de nascimento. seu algoritmo deverá mostrar na tela o nome da pessoa e a idade que ele tem ou terá até o fim de 2025. por exemplo, supondo que a pessoa informe o ano de nascimento como 1986 seu programa deverá imprimir: Fulano de tal tem (ou terá) 39 anos.

nome = input("Digite seu nome: ")
anonasc = int(input("Digite o ano de seu nascimento: "))

idade = 2025 - anonasc

print(f"Seu nome é {nome} e você tem ou terá {idade} anos de idade.")