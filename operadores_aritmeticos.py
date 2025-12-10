# + adição
# - subtração
# * multiplicação
# / divisão
# ** potencia
# // divisão inteira
# % resto da divisão

#ORDEM DE PRECEDENCIA

#1 ()
#2 **
#3 * / // %
#4 + -

N1 = int(input("Escreva um valor "))
N2 = int(input("Outro valor "))
S = N1 + N2
M = N1 * N2
D = N1 / N2
DI = N1 // N2
E = N1 ** N2

print("A soma vale {},\n o produto {} e a \n divisão {}".format(S, M, D), end=' ')
print("Divisão inteira {} e potencia {}".format(DI, E))

 