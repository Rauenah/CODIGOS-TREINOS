#manipulação de texto em Python te dá ferramentas para trabalhar 
#com strings de forma flexível, seja para limpeza de dados, análise ou formatação.


frase = "O tempo só anda de ida"
print(frase[13:])

#TRANFORMAR EM MAIUSCULAS UPPER

print(frase.upper())  # "O TEMPO SÓ ANDA DE IDA"

#TRANSFORMAR EM MINUSCULAS LOWER

print(frase.lower()) # "o tempo só anda de ida"

#CONTAR CARACTERES

print(len(frase)) #22

#FATIAR APAGAR PARTE DO TEXTO

print(frase[0:6])  # "O temp"

#SUBSTITUIR PALAVRAS REPLACE

print(frase.replace("ida", "volta"))   # "O tempo só anda de volta"

#DIVIDIR PALAVRAS SLIT

print(frase.split())  # ["O", "tempo", "só", "anda", "de", "ida"]

#VERIFICAR SE TEM UMA PALAVRA

print("tempo" in frase) #TRUE

#INVERTER TEXTO

print(frase[:: -1])  # "adi ed adna ós opmet O"




