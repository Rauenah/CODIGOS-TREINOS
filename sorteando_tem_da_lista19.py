#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

primeiro_nome = str(input("Leia o primeiro nome: "))
segundo_nome = str(input("Leia o segundo nome: "))
terceiro_nome = str(input("Leia o terceiro nome: "))
quarto_nome = str(input("Leia o quarto nome: "))
lista = [primeiro_nome,segundo_nome, terceiro_nome, quarto_nome]
escolhido = random.choice(lista)
print("O aluno escolhido foi {}".format(escolhido))