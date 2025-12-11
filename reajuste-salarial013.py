# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

salario= float(input("Qual o seu salario R$? "))
salario_reajustado = salario +(salario *15 /100)
print("Seu salario {:.2f} recebeu o reajuste de 15 e agora é {:.2f}.".format(salario, salario_reajustado))