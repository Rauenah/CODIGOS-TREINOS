#esse código está usando alguns comandos usados na calculadora de fertilidade

import pandas as pd
from datetime import datetime, timedelta

eventos = []

def adicionar_evento (nome, dias):
    data_evento = datetime.today() + timedelta(days=dias)
    eventos.append((nome, data_evento))

print(" Agenda de compromissos" )    

while True:
    nome=input("Digite o nome do compromisso (ou ENTER para sair): ")
    professora = input("Qual o nome do professor " )
    evolução= input("Digite como está sua evolução: bom, ruim, regular): ")
    if nome == "":
        break
    dias=int(input("Em quantos dias será esse compromisso? " ))
    adicionar_evento(nome, dias)

#Criar DataFrame para salvar

df = pd.DataFrame(eventos, columns=["Compromisso", "Data"])

#exportar excel

df.to_excel("agenda.xlsx", index=False)

print("Agenda salva em 'agenda.xlsx'")
