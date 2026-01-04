#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
#Calcule e mostre o comprimento da hipotenusa.

'''cateto_oposto = float(input("Cumprimento do cateto oposto: "))
cateto_adjacente = float(input("Cumprimento do cateto adjacente: "))
hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
print("A hipotenusa vai medir {:.2f}".format(hipotenusa))'''

#Utilizando modulo

'''import math
cateto_oposto = float(input("Cumprimento do cateto oposto: "))
cateto_adjacente = float(input("Cumprimento do cateto adjacente: "))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print("A hipotenusa vai medir {:.2f}".format(hipotenusa))'''''

#Importando o metodo

from math import hypot
cateto_oposto = float(input("Cumprimento do cateto oposto: "))
cateto_adjacente = float(input("Cumprimento do cateto adjacente: "))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print("A hipotenusa vai medir {:.2f}".format(hipotenusa))
