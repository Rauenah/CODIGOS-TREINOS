#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#considerando o dolar do dia 10/12/2025 U$$ 1,00 = R$ 5,19

real = float(input("Qual a quantidade de dinheiro que você tem? R$  "))
dólar = real / 5.19
print("Com R$ {:.2f} você pode comprar U$$ {:.2f}".format(real, dólar))
