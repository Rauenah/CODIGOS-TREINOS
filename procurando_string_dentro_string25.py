#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input("Escreva seu nome completo: ")).strip()

# Quebra o nome em partes (lista de palavras)
partes = nome.lower().split()

# Verifica se 'silva' está em alguma parte
tem_silva = "silva" in partes

print("Seu sobrenome é Silva? {}".format(tem_silva))
