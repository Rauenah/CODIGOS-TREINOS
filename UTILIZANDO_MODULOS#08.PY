#Em Python, módulos são arquivos que contêm código (funções, classes, variáveis) que podem ser reutilizados em diferentes programas. 
#Eles ajudam a organizar e estruturar o código, evitando repetição e facilitando a manutenção.
#• 	Normalmente, cada módulo é um arquivo com extensão .
#Eles servem para organizar o código em partes menores e mais fáceis de manter.


from math import sqrt, floor           #ctrl + espaço mostra o que tem no modulo
numero = int(input("Digite um número: "))
raiz = sqrt(numero)
print("A raiz de {} é igual a {:.2f}.".format(numero, floor(raiz)))


    #FAZER EXERCICIOS DO MODULO 8

#Quando você escreve IMPORT MATH , está trazendo para o seu programa o módulo MATH , que já vem na biblioteca padrão do Python.
#Esse módulo contém funções matemáticas prontas, como  (raiz quadrada), MATH.PI  (constante π), etc.

#TIPOS DE MÓDULOS

#Modulos embutidos: (built-in): ja vêm com o Python, como MATH, OS, SYS, RANDOM

#Módulos criados por voce: basta salvar um arquivo .PY e imnportar em outro código

#Módulos externos: instalados como PIP, como NUMPY, PANDAS, REQUESTS