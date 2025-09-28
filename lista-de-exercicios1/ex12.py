#o RM de um aluno da FIAP é composto por 5 dígitos. sua tarefa é escrever um algoritmo que recebe um RM e retorna a somatória de todos os dígitos do RM. por exemplo, suponha que o aluno tenha o RM 56395, seu algoritmo deverá imprimir como saída 28 = 5 + 6 + 3 + 9 + 5. dica: realize várias divisões e restos de divisões por 10.

rm = int(input("RM: "))
rm_aux = rm
ac = 0 #acumulador

resto = rm % 10
ac = ac + resto
rm = rm // 10

resto = rm % 10
ac = ac + resto
rm = rm // 10

resto = rm % 10
ac = ac + resto
rm = rm // 10

resto = rm % 10
ac = ac + resto
rm = rm // 10

resto = rm % 10
ac = ac + resto
rm = rm // 10

#Estamos reciclando a variável RM. às vezes não será possível, mas neste caso é aconselhável.

print(f"A soma do RM {rm_aux} vale {ac}.")