#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

#Resumo rápido:
#Seno, cosseno e tangente são razões trigonométricas usadas para relacionar os lados de um triângulo retângulo com seus ângulos. 
#Elas servem para calcular distâncias, alturas e ângulos em problemas de geometria, física, engenharia e até navegação

#Para que servem:
#• 	Geometria: calcular lados e ângulos de triângulos.
#• 	Física: decompor forças, movimentos e ondas.
#• 	Engenharia/Arquitetura: medir alturas, distâncias inacessíveis, inclinações.
#• 	Navegação e Astronomia: localizar posições e trajetórias.

#Imagine um prédio de 50 m de altura e você está a 30 m de distância da base.
#• 	O seno ajuda a calcular o ângulo de visão para o topo.
#• 	O cosseno ajuda a calcular a distância horizontal.
#• 	A tangente relaciona diretamente altura e distância

import math

angulo = float(input("Digite o angulo que você deseja: "))
seno = math.sin(math.radians(angulo))
print("O angulo de {} tem SENO de {:.2f}".format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print("O angulo de {} tem o COSSENO {:.2f} ".format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print("O angulo de {} tem a TANGENTE {:.2F} ".format(angulo, tangente))