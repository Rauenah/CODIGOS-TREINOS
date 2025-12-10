#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida =  float(input("Uma distância em metros: "))
centimetros = medida * 100
milimetros = medida * 1000
print("A média de {} medida corresponde a {} centimetros e {} milimetros".format(medida, centimetros, milimetros))
                