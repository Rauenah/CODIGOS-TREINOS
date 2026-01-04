#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

'''import math
numero= float(input("Digite um valor: "))
print("O valor digitado foi {} e a sua porção inteira é {}.".format(numero, math.trunc(numero)))'''

#Outra maneira de usar o import 

'''from math import trunc
numero = float(input("Digite um numero: "))
print("O valor digitado foi {} e a sua porção inteira é {}. ". format(numero, trunc(numero)))'''

#Nem sempre será necessario importar modulos, há outra maneira de usar o código obtendo o mesmo resultado

numero = float(input("Digite um número: "))
print("O valor digitado foi {} e a sua porção inteira é {}.".format(numero, int(numero)))