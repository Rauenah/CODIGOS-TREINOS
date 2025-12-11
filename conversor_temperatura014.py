#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input("Informe a temperatura em celsius "))
fahrenheit = ((9 * celsius)/ 5) + 32
print("A temperatura convertida de celsius {} para fahrenheit {}. ".format(celsius, fahrenheit))
