#esse código está usando alguns comandos usados na calculadora de fertilidade

from datetime import datetime

def calcular_idade (data_nascimento):
    nascimento =datetime.strptime(data_nascimento, "%d/%m/%Y")
    hoje = datetime.today()
    idade = hoje.year - nascimento.year

    if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
        idade -=1
    
    return idade 
    
print(" Calculadora idade  ")    
data = input ("Digite sua data de nascimento (dd/mm/aaaa):  ")
print(f"Você tem {calcular_idade(data)} anos.  ")