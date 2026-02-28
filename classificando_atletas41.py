# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, 
# de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JÚNIOR
#Até 25 anos: SÊNIOR
#Acima de 25 anos: MASTER

from datetime import date

atual = date.today().year
nascimento = int(input("Em que ano você nasceu? "))
idade = atual - nascimento
print("O atleta tem {} anos".format(idade))

if idade <=9:
    print("Você está na categoria MIRIM")
elif idade > 9 and idade <=14:
    print("Vocé está na classificação INFANTIL")
elif idade <=19:
    print("Classificação JUNIOR")
elif idade <= 25:
    print("Você está na classificação SÊNIOR")
else:
    print("Você está na categoria MASTER")








