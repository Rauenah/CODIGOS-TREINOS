#Escreva um programa que leia dois números inteiros e compare-os. 
# mostrando na tela uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais

numero1 = int(input("O primeiro numero "))
numero2= int(input("O segundo numero "))
if numero1 > numero2:
    print("O PRIMEIRO valor é MAIOR")
elif numero2 > numero1:
    print("O SEGUNDO numero é maior")
else:
    print("OS DOIS valores são IGUAIS")
