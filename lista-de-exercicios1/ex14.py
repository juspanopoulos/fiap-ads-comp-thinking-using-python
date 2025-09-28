#As casas de São Paulo estão recebendo o carnê do IPTU com duas opções de pagamento: à vista ou em 10 vezes. Sua tarefa é desenvolver um programa/algoritmo onde o usuário informa (digita) o valor total à vista e o valor de cada parcela. Seu programa imprime o desconto em percentual dado pela prefeitura para pagamento à vista.

vista = float(input("Preço do IPTU à vista: "))
parcela = float(input("Preço das parcelas do IPTU: "))

totalparcela = parcela * 10
desconto = totalparcela - vista
descontoporc = (desconto / totalparcela) * 100

#Exemplo numérico simples:
#À vista: R$ 900
#Parcelado: 10 x R$ 100 → R$ 1000
#Desconto em reais = 1000 - 900 = 100
#Qual porcentagem 100 é de 1000?
#100 / 1000 * 100 = 10%
#Então: o pagamento à vista tem 10% de desconto em relação ao valor parcelado. 

print(f"Seu desconto é de {descontoporc}% ao pagar à vista.")