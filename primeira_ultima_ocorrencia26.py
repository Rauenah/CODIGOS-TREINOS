#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", 
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input("Leia a frase escrita ")).upper().strip()
print("A letra A aparece {} vezes na frase".format(frase.count("A")))
print("A primeira letra A apareceu na posição {}".format(frase.find("A")+1))
print("A ultima vez que a letra A apareceu {}".format(frase.rfind("A")+1))

#R find = procure do lado direito