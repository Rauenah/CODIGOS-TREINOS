from datetime import datetime
from zoneinfo import ZoneInfo

#entrada de dados

data_str = input ("Data e hora(dd/mm/aaaa  HH:MM): ")
fuso_origem = input ("Fuso de origem (ex.: America/Sao_Paulo): ")
fuso_destino = input ("Fuso de destino (ex.: Europe/Paris): ")

#conversão

data =datetime.strptime(data_str, "%d/%m/%Y  %H:%M")
data_origem = data.replace (tzinfo=ZoneInfo(fuso_origem))
data_destino= data_origem.astimezone(ZoneInfo(fuso_destino))

#saida

print("Origem:", data_origem.strftime("%d/%m/%Y %H:%M %Z"))
print("Destino:", data_destino.strftime("%d/%m/%Y %H:%M %Z"))

